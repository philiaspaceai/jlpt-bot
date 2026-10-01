"""Level select regression test: the edited setup message must show the
user's actual choice, not snap back to N5.

Root cause (discord.py 2.7.1, verified in .venv discord/ui/select.py):
`Select.to_component_dict()` serializes the option list *including each
option's `default` flag*. The user's transient pick (`_values`) is NOT part
of the payload. So editing the message with a view whose options still mark
N5 as default re-renders N5 as selected, even though the bot stored N4.
"""

from unittest.mock import AsyncMock

import pytest

from jlpt_bot.config import Settings
from jlpt_bot.quiz import QuizManager
from jlpt_bot.store import QuestionStore
from jlpt_bot.views import SetupView


def _payload_defaults(view: SetupView) -> dict[str, str]:
    data = view.level_select.to_component_dict()
    return {o["value"]: o.get("default", False) for o in data["options"]}


@pytest.mark.asyncio
async def test_level_choice_survives_message_edit():
    store = QuestionStore.load("data")
    view = SetupView(store=store, manager=QuizManager(),
                     settings=Settings(token="x", guild_id=1, channel_id=2))
    # Simulate Discord delivering the user's pick (what _handle_submit does).
    view.level_select._values = ["N4"]  # type: ignore[attr-defined]
    interaction = AsyncMock()
    interaction.guild_id = 1
    interaction.channel_id = 2

    await view._on_level(interaction)

    assert view.level == "N4"
    interaction.response.edit_message.assert_awaited_once()
    sent_view = interaction.response.edit_message.call_args.kwargs["view"]
    defaults = _payload_defaults(sent_view)
    assert defaults.get("N4") is True
    assert defaults.get("N5") is not True


@pytest.mark.asyncio
async def test_type_choice_survives_level_refresh():
    store = QuestionStore.load("data")
    view = SetupView(store=store, manager=QuizManager(),
                     settings=Settings(token="x", guild_id=1, channel_id=2))
    view.level_select._values = ["N3"]  # type: ignore[attr-defined]
    interaction = AsyncMock()
    interaction.guild_id = 1
    interaction.channel_id = 2

    await view._on_level(interaction)

    sent_view = interaction.response.edit_message.call_args.kwargs["view"]
    type_data = sent_view.type_select.to_component_dict()
    defaults = [o for o in type_data["options"] if o.get("default")]
    # Exactly one default, and it must be a real option of the new level.
    assert len(defaults) == 1
    assert defaults[0]["value"] in {o["value"] for o in type_data["options"]}
