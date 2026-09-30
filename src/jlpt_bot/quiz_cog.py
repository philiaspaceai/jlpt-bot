"""Quiz cog with /jq start and the 5-minute idle watcher.

discord.py 2.7.1, see:
- docs/discord-py/ext-commands-api.md (Cog)
- docs/discord-py/interactions-api.md (app_commands.Group, Interaction)
- docs/discord-py/ext-tasks-index.md (tasks.loop)
"""

from __future__ import annotations

import logging

import discord
from discord import app_commands
from discord.ext import commands, tasks

from . import embeds
from .config import Settings
from .quiz import QuizManager
from .store import QuestionStore
from .views import QuizView, SetupView

log = logging.getLogger("jlpt_bot.cog")


class QuizCog(commands.Cog):
    def __init__(self, bot: commands.Bot, settings: Settings, store: QuestionStore, manager: QuizManager):
        self.bot = bot
        self.settings = settings
        self.store = store
        self.manager = manager
        self.idle_watcher.start()

    def cog_unload(self) -> None:
        self.idle_watcher.cancel()

    jq = app_commands.Group(name="jq", description="JLPT quiz commands")

    @jq.command(name="start", description="Start a JLPT quiz setup")
    async def jq_start(self, interaction: discord.Interaction) -> None:
        if interaction.guild_id != self.settings.guild_id or interaction.channel_id != self.settings.channel_id:
            await interaction.response.send_message(embed=embeds.guard_embed(), ephemeral=True)
            return
        existing = await self.manager.get()
        if existing is not None:
            await interaction.response.send_message(embed=embeds.busy_embed(), ephemeral=True)
            return
        view = SetupView(store=self.store, manager=self.manager, settings=self.settings)
        await interaction.response.send_message(embed=embeds.setup_embed(), view=view, ephemeral=True)
        log.info("setup opened by %s (%s)", interaction.user, interaction.user.id)

    @tasks.loop(seconds=30.0)
    async def idle_watcher(self) -> None:
        session = await self.manager.get()
        if session is None:
            return
        if session.idle_seconds() < self.settings.idle_timeout_sec:
            return
        log.info("session %s idle timeout (%.0fs)", session.session_id, session.idle_seconds())
        session.close()
        channel = self.bot.get_channel(self.settings.channel_id)
        try:
            if channel is not None and isinstance(channel, discord.abc.Messageable):
                # Try to update the quiz message if we know it.
                if session.message_id is not None:
                    try:
                        msg = await channel.fetch_message(session.message_id)  # type: ignore[attr-defined]
                        dead = QuizView(session=session, manager=self.manager, settings=self.settings)
                        for child in dead.children:
                            child.disabled = True  # type: ignore[attr-defined]
                        await msg.edit(embed=embeds.timeout_embed(session), view=dead)
                    except Exception:
                        await channel.send(embed=embeds.timeout_embed(session))  # type: ignore[attr-defined]
                else:
                    await channel.send(embed=embeds.timeout_embed(session))  # type: ignore[attr-defined]
        except Exception:
            log.exception("failed to post timeout message")
        finally:
            await self.manager.stop()

    @idle_watcher.before_loop
    async def _before_idle(self) -> None:
        await self.bot.wait_until_ready()
