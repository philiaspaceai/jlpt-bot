"""Guard + config tests: single server/channel enforcement."""

import os

from jlpt_dojo.config import Settings, is_allowed_context, load_settings


def test_guard_allows_only_configured():
    s = Settings(token="x", guild_id=1, channel_id=2)
    assert is_allowed_context(1, 2, s) is True
    assert is_allowed_context(1, 999, s) is False
    assert is_allowed_context(999, 2, s) is False
    assert is_allowed_context(None, None, s) is False


def test_load_settings_validates(monkeypatch):
    monkeypatch.setattr("dotenv.load_dotenv", lambda *a, **k: False)
    monkeypatch.setenv("DISCORD_TOKEN", "tok")
    monkeypatch.setenv("JLPT_GUILD_ID", "10")
    monkeypatch.setenv("JLPT_CHANNEL_ID", "20")
    s = load_settings()
    assert (s.guild_id, s.channel_id) == (10, 20)


def test_load_settings_missing(monkeypatch):
    monkeypatch.setattr("dotenv.load_dotenv", lambda *a, **k: False)
    monkeypatch.delenv("DISCORD_TOKEN", raising=False)
    monkeypatch.setenv("JLPT_GUILD_ID", "10")
    monkeypatch.setenv("JLPT_CHANNEL_ID", "20")
    try:
        load_settings()
    except RuntimeError as exc:
        assert "DISCORD_TOKEN" in str(exc)
    else:
        raise AssertionError("expected RuntimeError")
