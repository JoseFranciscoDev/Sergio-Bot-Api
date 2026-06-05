from fastapi import APIRouter, Depends, Query, status, HTTPException
from api.v1.Users.services import UserService, get_user_service
from api.v1.Users.schemas import (
    FiltersSchema,
    CreateUserSchema,
    UpdateUserSchema,
    UserResponseSchema,
)
from api.v1.Users.exceptions import UserAlreadyExistsError, UserNotFoundError

router = APIRouter(prefix="/users", tags=["Users - V1"])


@router.get("/", response_model=list[UserResponseSchema])
def get_users(
    filters_query: FiltersSchema = Query(),
    service: UserService = Depends(get_user_service),
):
    return service.get_users(
        filters_query.limit,
        filters_query.page,
        filters_query.order_by,
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseSchema)
def post_users(
    new_user: CreateUserSchema,
    service: UserService = Depends(get_user_service),
):
    try:
        return service.create_user(new_user)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def put_user(
    user_id: int,
    data: UpdateUserSchema,
    service: UserService = Depends(get_user_service),
):
    try:
        return service.update_user(user_id, data)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    try:
        service.soft_delete_user(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
