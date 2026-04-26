from fastapi import APIRouter, Depends, Query
from api.v1.Users.services import UserService
from api.v1.Users.services import get_user_service
from api.v1.Users.schemas import FiltersSchema

router = APIRouter(prefix="/users", tags=["Users - V1"])


@router.get("/")
def get_users(
    filters_query: FiltersSchema = Query(),
    service: UserService = Depends(get_user_service),
):
    users = service.get_users(filters_query.limit, filters_query.page)
    return users
