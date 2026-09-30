"""Bot factory. discord.py 2.7.1, see docs/discord-py/ext-commands-api.md (Bot)."""

from __future__ import annotations

import logging

import discord
from discord.ext import commands

from .config import Settings
from .quiz import QuizManager
from .store import QuestionStore

log = logging.getLogger("jlpt_bot.bot")


def build_bot(settings: Settings, store: QuestionStore, manager: QuizManager) -> commands.Bot:
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.settings = settings  # type: ignore[attr-defined]
    bot.store = store  # type: ignore[attr-defined]
    bot.quiz_manager = manager  # type: ignore[attr-defined]

    from .quiz_cog import QuizCog

    async def _setup_hook() -> None:
        await bot.add_cog(QuizCog(bot, settings, store, manager))
        # Sync slash commands to the single guild for instant availability.
        try:
            guild = discord.Object(id=settings.guild_id)
            bot.tree.copy_global_to(guild=guild)
            await bot.tree.sync(guild=guild)
            log.info("slash commands synced to guild %s", settings.guild_id)
        except Exception:
            log.exception("failed to sync slash commands")

    bot.setup_hook = _setup_hook  # type: ignore[method-assign]

    @bot.event
    async def on_ready() -> None:
        log.info("logged in as %s", bot.user)

    @bot.event
    async def on_error(event: str, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        log.exception("unhandled error in event %s", event)

    return bot
