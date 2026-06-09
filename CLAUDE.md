# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A FastAPI backend API with SQLAlchemy (MySQL) for managing users and transactions, with planned Gemini API integration.

## Commands

All commands run from `Sergio-Bot-Api/` with the venv activated.

```bash
# Activate venv (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run dev server
fastapi dev main.py

# Run all tests
pytest

# Run a single test file
pytest api/v1/tests/user_test.py

# Run a single test by name
pytest api/v1/tests/user_test.py::test_create_user
```

Tests hit a real MySQL database — the test suite requires the DB to be running and `DB_URL` set in `.env`.

## Architecture

Each domain module under `api/v1/<Module>/` follows a strict four-layer pattern:

```
router.py       → HTTP endpoints, FastAPI Depends injection
services.py     → business logic, orchestrates repository calls
repository.py   → database queries via SQLAlchemy Session
models.py       → SQLAlchemy ORM table definitions (inherit from Base)
schemas.py      → Pydantic request/response models
exceptions.py   → domain-specific exception classes
```

**Dependency injection chain:** `get_db()` (yields a Session) → `get_<module>_repository()` → `get_<module>_service()` — all wired through FastAPI's `Depends`.

**Database:** `api/v1/shared/base.py` defines `Base` (the SQLAlchemy `DeclarativeBase` shared by all models). Models must import `Base` from `base.py` — never from `database.py` — to avoid circular imports. `api/v1/shared/database.py` imports `Base` from `base.py`, then imports all models (via `from api.v1.<Module>.models import *`) so `Base.metadata.create_all` picks them up, and defines `engine`, `Session`, `init_db()`, and `get_db()`.

**Settings:** `api/v1/shared/settings.py` uses `pydantic-settings` to load env vars from the `.env` file at the project root. Add new config values to the `Settings` class there.

**Routing:** `api/v1/routers.py` is the single aggregator — add `include_router()` calls here when creating a new module. The top-level `main.py` mounts this under no prefix; the v1 router sets `prefix="/v1"`.

## Adding a new domain module

1. Create `api/v1/<Module>/` with the five files above.
2. Import the new model in `api/v1/shared/database.py`.
3. Register the new router in `api/v1/routers.py`.

## Environment

`.env` at root (loaded by pydantic-settings):

## Restrictions

Never modify functions/methods that dont have explicity requested to you modify