from fastapi import APIRouter
from api.v1.Users.router import router as users_router

router = APIRouter(prefix="/v1", tags=["V1"])

router.include_router(users_router)
