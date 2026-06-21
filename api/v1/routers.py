from fastapi import APIRouter
from api.v1.Users.router import router as users_router
from api.v1.Conversation.router import router as conversations_router
from api.v1.Message.router import router as messages_router

router = APIRouter(prefix="/v1", tags=["V1"])

router.include_router(users_router)
router.include_router(conversations_router)
router.include_router(messages_router)
