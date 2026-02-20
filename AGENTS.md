# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the Gradio entry point (Blocks definition).
- `PRD.md` and `FEATURES.md` capture product scope and user requests; keep behavior aligned with them.
- `CLAUDE.md` is the authoritative internal guide; this document follows it and should be updated when it changes.
- Expected module layout per `CLAUDE.md`: `tabs/` contains tab implementations like `tab01_chat.py`, `tab10_apikey.py`.
- `pyproject.toml` and `.python-version` define Python 3.11 and packaging metadata.

## Build, Test, and Development Commands
- `uv sync` installs dependencies declared in `pyproject.toml`.
- `uv run python main.py` runs the app locally.
- `uv add <package-name>` adds a dependency and updates the lockfile.

## Coding Style & Naming Conventions
- Use 4-space indentation and standard Python naming (`snake_case` for functions/vars, `PascalCase` for classes).
- Keep the entry point in `main.py`, and place tab implementations under `tabs/` with `tabNN_*.py` naming.
- No formatter or linter is configured yet; if you add one (e.g., Ruff, Black), update this guide and `pyproject.toml`.

## Testing Guidelines
- There is no test suite configured today.
- If you introduce tests, prefer `tests/` with `pytest`-style naming (`test_*.py`) and document the test command here.

## Commit & Pull Request Guidelines
- Git history currently has a single “Initial commit”; no commit-message convention is established.
- Follow the workflow in `CLAUDE.md`: issue-based development, branch per issue, and PR for review.
- PRs should include a short summary, testing notes (even if “not run”), and UI screenshots when relevant.
- Team communication is expected to be in Japanese per `CLAUDE.md`.

## Security & Configuration Tips
- Never commit API keys or secrets. Use `GEMINI_API_KEY` via environment variables or local `.env`.
- Do not log or persist API keys; if a UI input exists, it should be session-scoped and take precedence.
- When running Gradio, bind to `server_name=\"0.0.0.0\"` and set `server_port=int(os.environ.get(\"PORT\", 7860))`.

## Architecture Overview
- Target stack per `CLAUDE.md`: Python 3.11, Gradio 6 UI, Google ADK (Gemini), deploy to GCP Cloud Run.
- The app is a 10-tab experimental UI; keep tabs modular under `tabs/`.

## リポジトリ

- GitHub: <https://github.com/catnipglitch/gradio6-playground>
- SSH: `git@github.com:catnipglitch/gradio6-playground.git`
