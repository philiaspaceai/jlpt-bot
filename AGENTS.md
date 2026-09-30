# AGENTS.md — jlpt-bot

## Stack (pinned)
- `discord.py==2.7.1` — do not upgrade without checking `docs/discord-py/` first.
  Authority: `api.md`, `ext-commands-api.md`, `ext-tasks-index.md`, `interactions-api.md`.
- Python `>=3.14` via `uv` (auto-provisions). Entrypoint is `uv run jlpt-bot`
  (`[project.scripts]` → `src/jlpt_bot/__main__.py:main`). Production runs
  `./start.sh`, which is what `systemd/jlpt-bot.service` executes.

## Commands
- `uv sync --group dev` then `uv run pytest -v`
- Single file: `uv run pytest tests/test_quiz.py -v`
- Async tests need `@pytest.mark.asyncio` (`asyncio_mode = "strict"`).

## Architecture (one-way, keep it)
- Pure (never import `discord`): `config.py`, `models.py`, `store.py`, `quiz.py`, `categories.py`
- Discord layer: `bot.py`, `quiz_cog.py`, `views.py`, `embeds.py`
- Direction: discord layer → `quiz.py` → `store.py/models.py` → `config.py`;
  `categories.py` is a leaf (no repo imports) used by `store.py` + `views.py`.
  Never reverse. All `Embed` builders live in `embeds.py`; all
  `View/Select/Button` in `views.py`.

## Quiz semantics (don't change silently)
- One active session per process (`QuizManager` + `asyncio.Lock`); second
  `/jq start` must be rejected with `busy_embed`.
- Fastest correct +1 then auto-advance; wrong/stale presses are ephemeral-only.
- Fresh `QuizView` per question; staleness is detected via `question_index`.
- `Stop` only starter or `administrator`/`manage_guild`.
- Idle close via `tasks.loop(30s)` vs `JLPT_IDLE_TIMEOUT_SEC` (min 60).
- No category column in data: 3 broad categories from `categories.classify()`
  (vocab/grammar/reading) over normalized `instruction` text; data/*.json
  must never be edited. Counts: 5/10/15/20.
  Trap: numbered passage blanks (19–23, 41–45) are grammar, but multi-part
  headers like `次の(1)から(3)の文章を読んで` are reading — a generic
  `\(\d+\)から\(\d+\)` regex misfiles ~200 questions. `test_categories.py`
  snapshot counts lock the mapping; update them deliberately.
- Anti-memorization: `shuffle_options()` per session, remap answer, never send
  original order. Embed size limits are enforced by `test_embeds.py`.

## Gotchas
- `load_settings()` calls `dotenv.load_dotenv()` internally, so a real `.env`
  leaks into tests. Settings tests must stub it:
  `monkeypatch.setattr("dotenv.load_dotenv", lambda *a, **k: False)` (see
  `tests/test_guards.py` — this exact bug failed only on the VPS).
- Single server/channel guard (`is_allowed_context`) must be checked in every
  interaction callback, not just `/jq start`.
- Over SSH `uv` is not on `PATH`: use `/root/.local/bin/uv` absolute path
  (deploy workflow already does this; bare `uv` fails with exit 127).

## Secrets (history was purged once — don't reintroduce)
- Never commit real token/guild/channel IDs. `.env.example` uses placeholders;
  `.env` and `log.txt` are gitignored. Real env lives only at
  `/root/jlpt-bot/.env` (mode 600).
- Deploy (`deploy.yml`) is `git pull --ff-only` + `uv sync --frozen` +
  `systemctl restart jlpt-bot` via `VPS_*`/`SSH_PRIVATE_KEY` secrets.
  After any history rewrite, ff-only breaks: fix VPS with
  `git fetch origin --prune && git reset --hard origin/main`.
- VPS shares `/root` with `ruri/hinari/ayumi/phix`: only touch
  `/root/jlpt-bot` and the `jlpt-bot` service.
