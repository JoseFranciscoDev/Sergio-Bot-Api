import pytest
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from api.v1.shared.settings import settings
from api.v1.Users.models import User


@pytest.fixture(autouse=True)
def clean_users_table():
    yield
    engine = create_engine(settings.DB_URL)
    with sessionmaker(engine)() as session:
        session.execute(delete(User))
        session.commit()
