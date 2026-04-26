from fastapi import Depends
from sqlalchemy.sql.selectable import Select
from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session
from api.v1.Users.models import User
from api.v1.shared.database import get_db


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self, limit, offset) -> Sequence[User]:
        query: Select[tuple[User]] = select(User).offset(offset).limit(limit)
        users: Sequence[User] = self.session.execute(query).scalars().all()
        return users


def get_user_repository(session: Session = Depends(get_db)):
    return UserRepository(session)
