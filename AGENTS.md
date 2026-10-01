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
- Pure (never import `discord`): `config.py`, `models.py`, `store.py`, `quiz.py`, `categories.py`,
  `progression.py`, `badges.py`, `render.py`
- Discord layer: `bot.py`, `quiz_cog.py`, `views.py`, `embeds.py`
- Infra: `db.py` (aiosqlite, single-writer lock)
- Direction: discord layer → `quiz.py` → `store.py/models.py` → `config.py`;
  `categories.py` is a leaf (no repo imports) used by `store.py` + `views.py`.
  `quiz_cog.py` implements `views.QuizHooks` (EXP/rank/badge writes live there,
  never in views). Never reverse. All `Embed` builders live in `embeds.py`; all
  `View/Select/Button` in `views.py`.
- Slash group `/jq`: `start`, `me`, `profile`, `leaderboard`, `info`, `badge`.
  All but `info` require the configured guild+channel (`_guarded`).

## Quiz semantics (don't change silently)
- One active session per process (`QuizManager` + `asyncio.Lock`); second
  `/jq start` must be rejected with `busy_embed`.
- First press decides each question (correct +1, wrong = mistake +1) and
  advances immediately — no brute-forcing. Mistakes never reduce EXP.
- New pipeline per question: strip buttons (keep content) → reveal message →
  next question as a NEW message (history preserved, see `test_answer_flow.py`).
- Fresh `QuizView` per question; staleness is detected via `question_index`.
- `Stop` only starter or `administrator`/`manage_guild`.
- On start, the ephemeral setup message is deleted (`delete_original_response`);
  only the public quiz + a followup note remain (see `test_setup_dismiss.py`).
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

## Progression (tuned in config.yaml — code reads, never hardcodes)
- 10 ranks Houga→Shindan (700k for Shindan, 1M lifetime ceiling); EXP only for
  the scorer, scaled by question level; level quotas gate each rank; trials
  for ranks 8–10 (rolling accuracy, wins, N1 streak).
- 10 badges, 8 display slots (`/jq badge` equip UI); conditions in `badges.py`,
  storage in `db.py`. Clean = session win with zero mistakes.
- Season DB is one SQLite file; rollover archives the whole file to
  `db/archive/` and starts fresh. Lifetime = current + archives.
- Profile PNGs render from `templates/` via WeasyPrint (`render.py`); rank art
  and themed icons ship under `src/jlpt_bot/assets/`. `design/` is review-only
  mockups, never imported by the bot.

## Design (review mockups in `design/`, gitignored)
- `profile-special.css` + per-rank sample HTML (`card-05-meijin.html` …,
  `card-10-shindan.html`) + `preview-*.png` renders. One rank look = one
  theme block in section 1; markup never changes per rank. Badge pills live
  in the same file (they need theme vars); per-rank badge exceptions
  (Meijin monochrome, Shindan legendary) sit next to the theme blocks.
- WeasyPrint-safe CSS only: flexbox (no grid), flat colors (no `color-mix`),
  no filters; locked/monochrome states are pre-rendered SVG files, and
  `text-shadow`/`box-shadow` are verified working — re-verify visually if used.
- Templates use `string.Template` `$VARS`; keep `$` out of CSS.

## Gotchas
- `load_settings()` calls `dotenv.load_dotenv()` internally, so a real `.env`
  leaks into tests. Settings tests must stub it:
  `monkeypatch.setattr("dotenv.load_dotenv", lambda *a, **k: False)` (see
  `tests/test_guards.py` — this exact bug failed only on the VPS).
- Single server/channel guard (`is_allowed_context`) must be checked in every
  interaction callback, not just `/jq start`.
- Over SSH `uv` is not on `PATH`: use `/root/.local/bin/uv` absolute path
  (deploy workflow already does this; bare `uv` fails with exit 127).
- After `edit_message(view=...)`, a Select snaps back to its initial option
  unless option `default` flags mirror the pick (`_sync_defaults` in
  `views.py`): discord.py 2.7.1 serializes only `default` flags, not the
  transient selection (see `tests/test_setup_select.py`).

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
