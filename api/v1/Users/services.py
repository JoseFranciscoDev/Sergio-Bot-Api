from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from api.v1.Users.repository import UserRepository, get_user_repository
from api.v1.Users.models import User
from api.v1.Users.schemas import CreateUserSchema, UpdateUserSchema
from api.v1.Users.exceptions import UserAlreadyExistsError, UserNotFoundError


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self, per_page: int, page: int, order_by: str = "id") -> list[User]:
        offset = (page - 1) * per_page
        return self.repository.get_users(limit=per_page, offset=offset, order_by=order_by)

    def create_user(self, new_user: CreateUserSchema) -> User:
        try:
            return self.repository.create_user(User(**new_user.model_dump()))
        except IntegrityError:
            raise UserAlreadyExistsError("Já existe um usuário com esse nome ou número")

    def update_user(self, user_id: int, data: UpdateUserSchema) -> User:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise UserNotFoundError(f"User {user_id} not found")
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(user, field, value)
        return self.repository.update_user(user)

    def soft_delete_user(self, user_id: int) -> None:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise UserNotFoundError(f"User {user_id} not found")
        self.repository.soft_delete_user(user)


def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
):
    return UserService(repository)
