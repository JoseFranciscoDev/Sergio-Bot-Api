from sqlalchemy import create_engine, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from api.v1.shared.settings import settings
from api.v1.Users.models import *  # noqa: F403


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)


engine = create_engine(settings.DB_URL)
Session = sessionmaker(engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    session_local = Session()
    try:
        yield session_local
    finally:
        session_local.close()
