from fastapi import Depends
from sqlalchemy import select, asc
from sqlalchemy.orm import Session
from api.v1.Users.models import User
from api.v1.shared.database import get_db


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self, limit: int, offset: int, order_by: str = "id") -> list[User]:
        order_col = getattr(User, order_by)
        query = select(User).order_by(asc(order_col)).offset(offset).limit(limit)
        return list(self.session.execute(query).scalars().all())

    def get_user_by_id(self, user_id: int) -> User | None:
        query = select(User).where(User.id == user_id, User.is_active == True)  # noqa: E712
        return self.session.execute(query).scalars().first()

    def create_user(self, new_user: User) -> User:
        try:
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return new_user
        except Exception:
            self.session.rollback()
            raise

    def update_user(self, user: User) -> User:
        try:
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception:
            self.session.rollback()
            raise

    def soft_delete_user(self, user: User) -> bool:
        try:
            user.is_active = False
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            raise


def get_user_repository(session: Session = Depends(get_db)):
    return UserRepository(session)
