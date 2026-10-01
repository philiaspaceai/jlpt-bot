"""Entrypoint: `uv run jlpt-bot`. discord.py 2.7.1, see docs/discord-py/api.md (Client.run)."""

from __future__ import annotations

import yaml

from .bot import build_bot
from .config import load_settings
from .db import Database
from .logging_setup import setup_logging
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
    with open(settings.config_path, encoding="utf-8") as fh:
        prog = yaml.safe_load(fh)
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
    db = Database(settings.db_path, settings.archive_dir)
    bot = build_bot(settings, store, manager, db, prog)
    # Client.run is blocking and handles the event loop (docs/discord-py/api.md).
    bot.run(settings.token, log_handler=None)


if __name__ == "__main__":
    main()
