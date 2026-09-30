"""Setup dismiss test: starting a quiz deletes the ephemeral setup message."""

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from jlpt_bot.config import Settings
from jlpt_bot.quiz import QuizManager
from jlpt_bot.store import QuestionStore
from jlpt_bot.views import SetupView


import discord


def _interaction(view: SetupView):
    user = SimpleNamespace(id=111, display_name="starter")
    channel = AsyncMock(spec=discord.abc.Messageable)
    channel.send.return_value = SimpleNamespace(id=999)
    return SimpleNamespace(
        guild_id=1,
        channel_id=2,
        user=user,
        response=AsyncMock(),
        followup=AsyncMock(),
        client=SimpleNamespace(get_channel=lambda _cid: channel),
        delete_original_response=AsyncMock(),
    ), channel


@pytest.mark.asyncio
async def test_start_deletes_setup_message():
    store = QuestionStore.load("data")
    manager = QuizManager()
    settings = Settings(token="x", guild_id=1, channel_id=2)
    view = SetupView(store=store, manager=manager, settings=settings)
    view.count = 5
    interaction, channel = _interaction(view)

    start_btn = next(c for c in view.children if getattr(c, "label", None) == "Start quiz")
    await start_btn.callback(interaction)

    # Public quiz posted exactly once...
    channel.send.assert_awaited_once()
    # ...and the setup embed is dismissed, leaving only a followup note.
    interaction.delete_original_response.assert_awaited_once()
    interaction.followup.send.assert_awaited_once()

    session = await manager.get()
    assert session is not None and session.total == 5
    await manager.stop()
