"""Environment-based configuration. No discord import allowed here."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    token: str
    guild_id: int
    channel_id: int
    data_dir: str = "data"
    log_path: str = "log.txt"
    idle_timeout_sec: int = 300


def _get_env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name, default)
    if value is not None:
        value = value.strip()
        if value == "":
            return default
    return value


def load_settings() -> Settings:
    """Load and validate settings. Fail fast with a clear message."""
    # Load .env file if present (optional, never required in production).
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
    except Exception:
        pass

    token = _get_env("DISCORD_TOKEN")
    guild_raw = _get_env("JLPT_GUILD_ID")
    channel_raw = _get_env("JLPT_CHANNEL_ID")
    data_dir = _get_env("JLPT_DATA_DIR", "data") or "data"
    log_path = _get_env("JLPT_LOG_PATH", "log.txt") or "log.txt"
    idle_raw = _get_env("JLPT_IDLE_TIMEOUT_SEC", "300") or "300"

    missing = [k for k, v in {"DISCORD_TOKEN": token, "JLPT_GUILD_ID": guild_raw, "JLPT_CHANNEL_ID": channel_raw}.items() if not v]
    if missing:
        raise RuntimeError(f"Missing required env vars: {', '.join(missing)}. See .env.example.")

    try:
        guild_id = int(guild_raw or "")
        channel_id = int(channel_raw or "")
    except ValueError as exc:
        raise RuntimeError("JLPT_GUILD_ID and JLPT_CHANNEL_ID must be integers.") from exc

    try:
        idle_timeout_sec = int(idle_raw)
    except ValueError as exc:
        raise RuntimeError("JLPT_IDLE_TIMEOUT_SEC must be an integer.") from exc
    if idle_timeout_sec < 60:
        raise RuntimeError("JLPT_IDLE_TIMEOUT_SEC must be >= 60.")

    if not token:
        raise RuntimeError("DISCORD_TOKEN is empty.")

    return Settings(
        token=token,
        guild_id=guild_id,
        channel_id=channel_id,
        data_dir=data_dir,
        log_path=log_path,
        idle_timeout_sec=idle_timeout_sec,
    )


def is_allowed_context(guild_id: int | None, channel_id: int | None, settings: Settings) -> bool:
    """Single-server / single-channel guard. Pure function for easy testing."""
    return guild_id == settings.guild_id and channel_id == settings.channel_id
