"""Discord Views (buttons/selects).

discord.py 2.7.1, see:
- docs/discord-py/interactions-api.md (discord.ui.View/Button/Select,
  Interaction, InteractionResponse.send_message/edit_message/defer, followup)
- docs/discord-py/api.md (discord.Embed, View registration)
"""

from __future__ import annotations

import logging
import random

import discord

from . import embeds
from .categories import ALL_LABEL, ALL_TYPES, BY_ID, CATEGORIES
from .config import Settings
from .models import QuizConfig
from .quiz import QuizManager, QuizSession
from .store import ALL_LEVELS, COUNT_CHOICES, QuestionStore, shuffle_options

log = logging.getLogger("jlpt_bot.views")


def _is_admin(interaction: discord.Interaction) -> bool:
    perms = getattr(interaction.user, "guild_permissions", None)
    if perms is None:
        return False
    return bool(getattr(perms, "administrator", False) or getattr(perms, "manage_guild", False))


class SetupView(discord.ui.View):
    """Level + type + count picker. Sent as an ephemeral message."""

    def __init__(self, store: QuestionStore, manager: QuizManager, settings: Settings, timeout: float = 180):
        super().__init__(timeout=timeout)
        self.store = store
        self.manager = manager
        self.settings = settings
        self.level: str = "N5"
        self.type_id: str = ALL_TYPES
        self.count: int = 10

        self.level_select = discord.ui.Select(
            placeholder="Level",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(label="N5", value="N5", default=True),
                discord.SelectOption(label="N4", value="N4"),
                discord.SelectOption(label="N3", value="N3"),
                discord.SelectOption(label="N2", value="N2"),
                discord.SelectOption(label="N1", value="N1"),
                discord.SelectOption(label="ALL levels (mixed)", value=ALL_LEVELS),
            ],
        )
        self.level_select.callback = self._on_level  # type: ignore[method-assign]
        self.add_item(self.level_select)

        self.type_select = discord.ui.Select(
            placeholder="Question type",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label="ALL types", value=ALL_TYPES, default=True)],
        )
        self.type_select.callback = self._on_type  # type: ignore[method-assign]
        self.add_item(self.type_select)

        self.count_select = discord.ui.Select(
            placeholder="Question count",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(label=str(c), value=str(c), default=(c == 10))
                for c in COUNT_CHOICES
            ],
        )
        self.count_select.callback = self._on_count  # type: ignore[method-assign]
        self.add_item(self.count_select)

        self._refresh_types()

    def _refresh_types(self) -> None:
        counts = self.store.category_counts(self.level)
        opts = [discord.SelectOption(label=ALL_LABEL, value=ALL_TYPES, default=True)]
        for cat in CATEGORIES:
            n = counts.get(cat.id, 0)
            if n == 0:
                continue
            opts.append(
                discord.SelectOption(
                    label=f"{cat.label} ({n})"[:100],
                    value=cat.id,
                    description=cat.description[:100],
                )
            )
        if self.type_id not in {o.value for o in opts}:
            self.type_id = ALL_TYPES
        # Rebuild select options in place.
        self.type_select.options = opts

    async def _on_level(self, interaction: discord.Interaction) -> None:
        self.level = self.level_select.values[0]
        self._refresh_types()
        await interaction.response.edit_message(view=self)

    async def _on_type(self, interaction: discord.Interaction) -> None:
        self.type_id = self.type_select.values[0]
        await interaction.response.defer()

    async def _on_count(self, interaction: discord.Interaction) -> None:
        self.count = int(self.count_select.values[0])
        await interaction.response.defer()

    @discord.ui.button(label="Start quiz", style=discord.ButtonStyle.success)
    async def start_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        # Double guard: single server/channel + single session.
        if interaction.guild_id != self.settings.guild_id or interaction.channel_id != self.settings.channel_id:
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        existing = await self.manager.get()
        if existing is not None:
            await interaction.response.send_message(embed=embeds.busy_embed(), ephemeral=True)
            return

        rng = random.Random()
        pool = self.store.sample(self.level, self.type_id, self.count, rng)
        if not pool:
            await interaction.response.send_message(embed=embeds.wrong_pool_embed(), ephemeral=True)
            return

        type_label = ALL_LABEL
        if self.type_id != ALL_TYPES:
            cat = BY_ID.get(self.type_id)
            if cat is not None:
                type_label = cat.label

        user = interaction.user
        name = getattr(user, "display_name", None) or getattr(user, "name", "player")
        config = QuizConfig(
            level=self.level,
            type_id=self.type_id,
            type_label=type_label,
            count=len(pool),
            starter_id=user.id,
            starter_name=name,
            guild_id=self.settings.guild_id,
            channel_id=self.settings.channel_id,
        )
        shuffled = [shuffle_options(q, rng) for q in pool]
        session = await self.manager.start(config, shuffled)
        if session is None:
            await interaction.response.send_message(embed=embeds.busy_embed(), ephemeral=True)
            return

        log.info(
            "session %s started by %s (%s) level=%s type=%s count=%s",
            session.session_id,
            name,
            user.id,
            self.level,
            self.type_id,
            len(pool),
        )
        # Acknowledge the ephemeral setup interaction, then post the public quiz.
        await interaction.response.defer(ephemeral=True)
        channel = interaction.client.get_channel(self.settings.channel_id)
        if channel is None or not isinstance(channel, discord.abc.Messageable):
            await self.manager.stop()
            await interaction.followup.send("Configured channel not found.", ephemeral=True)
            return
        view = QuizView(session=session, manager=self.manager, settings=self.settings)
        msg = await channel.send(embed=embeds.question_embed(session), view=view)  # type: ignore[attr-defined]
        session.message_id = msg.id
        session.touch()
        await interaction.followup.send(
            f"Quiz started in <#{self.settings.channel_id}> ({len(pool)} questions).",
            ephemeral=True,
        )

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary)
    async def cancel_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await interaction.response.edit_message(content="Setup cancelled.", embed=None, view=None)


class QuizView(discord.ui.View):
    """Per-question buttons 1-4 plus Stop. A fresh view is posted per question."""

    def __init__(self, session: QuizSession, manager: QuizManager, settings: Settings):
        super().__init__(timeout=None)
        self.session = session
        self.manager = manager
        self.settings = settings
        self.question_index = session.current_index

    async def _guard(self, interaction: discord.Interaction) -> bool:
        if interaction.guild_id != self.settings.guild_id or interaction.channel_id != self.settings.channel_id:
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return False
        if not self.session.active:
            await interaction.response.send_message("This session is closed.", ephemeral=True)
            return False
        return True

    async def _press(self, interaction: discord.Interaction, picked: int) -> None:
        if not await self._guard(interaction):
            return
        user = interaction.user
        name = getattr(user, "display_name", None) or getattr(user, "name", "player")
        result = await self.session.answer(
            user_id=user.id,
            display_name=name,
            picked=picked,
            question_index=self.question_index,
        )
        if result.kind == "stale":
            await interaction.response.send_message("Too late — we already moved on.", ephemeral=True)
            return
        if result.kind == "finished":
            await interaction.response.send_message("This session is closed.", ephemeral=True)
            return
        if result.kind == "wrong":
            await interaction.response.send_message("Not correct.", ephemeral=True)
            log.info("session %s q%s wrong by %s (%s)", self.session.session_id, self.question_index, name, user.id)
            return
        # Correct: fastest finger wins, auto-advance.
        log.info(
            "session %s q%s correct by %s (%s)",
            self.session.session_id,
            self.question_index,
            name,
            user.id,
        )
        if self.session.is_finished():
            await self.manager.clear_finished()
            # Disable all buttons on the final message.
            for child in self.children:
                child.disabled = True  # type: ignore[attr-defined]
            await interaction.response.edit_message(
                embed=embeds.finished_embed(self.session), view=self
            )
            await self.manager.stop()
            log.info("session %s finished", self.session.session_id)
            return
        # Post the next question as a fresh view so stale presses are detectable.
        next_view = QuizView(session=self.session, manager=self.manager, settings=self.settings)
        await interaction.response.edit_message(embed=embeds.question_embed(self.session), view=next_view)

    @discord.ui.button(label="1", style=discord.ButtonStyle.primary, custom_id="jlpt:1")
    async def b1(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._press(interaction, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.primary, custom_id="jlpt:2")
    async def b2(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._press(interaction, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.primary, custom_id="jlpt:3")
    async def b3(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._press(interaction, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.primary, custom_id="jlpt:4")
    async def b4(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._press(interaction, 4)

    @discord.ui.button(label="Stop", style=discord.ButtonStyle.danger, custom_id="jlpt:stop")
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        if not await self._guard(interaction):
            return
        user = interaction.user
        name = getattr(user, "display_name", None) or getattr(user, "name", "player")
        if not self.session.can_stop(user.id, _is_admin(interaction)):
            await interaction.response.send_message(
                "Only the quiz starter or a server admin can stop.", ephemeral=True
            )
            return
        sess = self.session
        sess.close()
        for child in self.children:
            child.disabled = True  # type: ignore[attr-defined]
        await interaction.response.edit_message(embed=embeds.stopped_embed(sess, name), view=self)
        await self.manager.stop()
        log.info("session %s stopped by %s (%s)", sess.session_id, name, user.id)
