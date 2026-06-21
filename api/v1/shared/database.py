from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.v1.shared.settings import settings
from api.v1.shared.base import Base  # noqa: F401
from api.v1.Users.models import *  # noqa: F401, F403
from api.v1.Conversation.models import *  # noqa: F401, F403
from api.v1.Message.models import *  # noqa: F401, F403

engine = create_engine(settings.DB_URL)
Session = sessionmaker(engine)


def get_db():
    session_local = Session()
    try:
        yield session_local
    finally:
        session_local.close()
