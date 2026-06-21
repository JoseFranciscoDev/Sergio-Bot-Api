from fastapi import APIRouter, Depends, status, HTTPException
from api.v1.Conversation.service import ConversationService, get_conversation_service
from api.v1.Conversation.schemas import CreateConversationSchema, ConversationResponseSchema
from api.v1.Conversation.exceptions import ConversationNotFoundError

router = APIRouter(prefix="/conversations", tags=["Conversations - V1"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ConversationResponseSchema)
def post_conversation(
    data: CreateConversationSchema,
    service: ConversationService = Depends(get_conversation_service),
):
    return service.create_conversation(data)


@router.get("/{conversation_id}", response_model=ConversationResponseSchema)
def get_conversation(
    conversation_id: int,
    service: ConversationService = Depends(get_conversation_service),
):
    try:
        return service.get_conversation_by_id(conversation_id)
    except ConversationNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
