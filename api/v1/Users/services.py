from fastapi import Depends
from sqlalchemy import Sequence
from api.v1.Users.repository import UserRepository
from api.v1.Users.models import User
from api.v1.Users.repository import get_user_repository
from api.v1.Users.schemas import CreateUserSchema


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self, per_page, page):
        offset = (page - 1) * per_page
        users: Sequence[User] = self.repository.get_users(
            limit=per_page,
            offset=offset,
        )

        return users

    def create_user(self, new_user: CreateUserSchema):
        create_user = self.repository.create_user(
            User(**new_user.model_dump()),
        )
        if isinstance(create_user, Exception):
            raise create_user
        return create_user


def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)
