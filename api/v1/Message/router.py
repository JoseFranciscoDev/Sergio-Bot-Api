from fastapi import APIRouter, Depends, status, HTTPException
from api.v1.Message.service import MessageService, get_message_service
from api.v1.Message.schemas import CreateMessageSchema, MessageResponseSchema
from api.v1.Conversation.exceptions import ConversationNotFoundError

router = APIRouter(prefix="/messages", tags=["Messages - V1"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MessageResponseSchema)
def post_message(
    data: CreateMessageSchema,
    service: MessageService = Depends(get_message_service),
):
    try:
        return service.create_message(data)
    except ConversationNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=list[MessageResponseSchema])
def get_messages(
    conversation_id: int,
    service: MessageService = Depends(get_message_service),
):
    try:
        return service.get_messages_by_conversation(conversation_id)
    except ConversationNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
