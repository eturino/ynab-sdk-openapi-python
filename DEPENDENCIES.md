# Dependency State

Last reviewed: 2026-11-16

State file for the `upgrade-deps` skill (rules: `~/.agents/custom-skills/upgrade-deps/SKILL.md`).
Full per-pass detail lives in `git log -p DEPENDENCIES.md uv.lock`.

## House rules

- **Package manager:** uv 0.11.18 (`mise.toml`), lockfile `uv.lock`. Gate: `[tool.uv] exclude-newer = "5 days"`.
- **Runtime:** Python 3.13.13 in `mise.toml`, but `uv sync` built the local `.venv` on Python 3.15. Pin it with `.python-version` or `[tool.uv] python` when the runtime row below lands.
- **Generated code:** regenerate from the OpenAPI spec, never hand-edit.
- **Green gate:** `uv run flake8` (CI's strict selection) and `uv run pytest`. CI runs both on every push.

## Major Upgrades Blocked

Every row below was deferred by Edu on 2026-11-16 ("not now, next deps pass"), not blocked upstream. Not tried yet.

| Package | Current | Latest | Blocker | Since | Re-checked | Last tried |
| ------- | ------- | ------ | ------- | ----- | ---------- | ---------- |
| Python (runtime, `mise.toml`) | 3.13.13 | 3.15.2 | Deferred. Also make uv and mise agree on one version | 2026-11-16 | 2026-11-16 | - |
| `actions/checkout` | v3 (SHA-pinned) | v5 | Deferred to the next pass | 2026-11-16 | 2026-11-16 | - |

## Upgrade history

- **2026-11-16** Poetry to uv migration landed (from June 2026), flake8 kept out of `.venv`.
