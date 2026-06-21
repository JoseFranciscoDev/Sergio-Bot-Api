# Sergio Bot API

A RESTful API built with FastAPI and SQLAlchemy for managing users, conversations, and messages, with planned Gemini AI integration.

## Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| **FastAPI** | 0.136.0 | Web framework |
| **SQLAlchemy** | 2.0.49 | ORM |
| **MySQL Connector** | 9.7.0 | Database driver |
| **Alembic** | 1.18.4 | Database migrations |
| **Pydantic** | 2.13.3 | Data validation & settings |
| **Uvicorn** | 0.45.0 | ASGI server |
| **Pytest** | 9.0.3 | Testing |

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file at the project root:

```env
DB_URL=mysql+mysqlconnector://user:password@localhost:3306/sergiobot
```

Run database migrations:

```bash
alembic upgrade head
```

Start the development server:

```bash
fastapi dev main.py
```

## API Endpoints

### Health Check

| Method | Path | Description |
|---|---|---|
| `GET` | `/status` | Returns API status |

---

### Users — `/v1/users`

| Method | Path | Description |
|---|---|---|
| `GET` | `/v1/users/` | List users (supports pagination and ordering) |
| `POST` | `/v1/users/` | Create a new user |
| `PUT` | `/v1/users/{user_id}` | Update a user |
| `DELETE` | `/v1/users/{user_id}` | Soft delete a user |

**Query params for `GET /v1/users/`:** `limit`, `page`, `order_by`

---

### Conversations — `/v1/conversations`

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/conversations/` | Create a new conversation |
| `GET` | `/v1/conversations/{conversation_id}` | Get a conversation by ID |

---

### Messages — `/v1/messages`

| Method | Path | Description |
|---|---|---|
| `POST` | `/v1/messages/` | Send a message to a conversation |
| `GET` | `/v1/messages/?conversation_id={id}` | List all messages in a conversation |

## Project Structure

```
api/v1/
├── Users/
│   ├── models.py       # User ORM model
│   ├── schemas.py      # Pydantic schemas
│   ├── repository.py   # Database queries
│   ├── services.py     # Business logic
│   ├── router.py       # HTTP endpoints
│   └── exceptions.py   # Domain exceptions
├── Conversation/
│   └── ...             # Same structure
├── Message/
│   └── ...             # Same structure
└── shared/
    ├── base.py         # SQLAlchemy declarative base
    ├── database.py     # Engine, session, init_db
    └── settings.py     # Pydantic settings (loads .env)
```

## Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest api/v1/tests/user_test.py

# Run a specific test
pytest api/v1/tests/user_test.py::test_create_user
```

> Tests require the database to be running and `DB_URL` set in `.env`.
