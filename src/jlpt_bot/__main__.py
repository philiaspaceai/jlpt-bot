"""Entrypoint: `uv run jlpt-bot`. discord.py 2.7.1, see docs/discord-py/api.md (Client.run)."""

from __future__ import annotations

import discord

from .bot import build_bot
from .config import load_settings
from .logging_setup import get_logger, setup_logging
from .quiz import QuizManager
from .store import QuestionStore


def main() -> None:
    settings = load_settings()
    logger = setup_logging(settings.log_path)
    logger.info(
        "starting jlpt-bot guild=%s channel=%s data=%s",
        settings.guild_id,
        settings.channel_id,
        settings.data_dir,
    )
    store = QuestionStore.load(settings.data_dir)
    logger.info(
        "loaded questions N5=%s N4=%s N3=%s N2=%s N1=%s",
        store.total("N5"),
        store.total("N4"),
        store.total("N3"),
        store.total("N2"),
        store.total("N1"),
    )
    manager = QuizManager()
    bot = build_bot(settings, store, manager)
    # Client.run is blocking and handles the event loop (docs/discord-py/api.md).
    bot.run(settings.token, log_handler=None)


if __name__ == "__main__":
    main()
