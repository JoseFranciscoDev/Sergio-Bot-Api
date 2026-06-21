from fastapi import Depends
from api.v1.Conversation.repository import ConversationRepository, get_conversation_repository
from api.v1.Conversation.models import Conversation
from api.v1.Conversation.schemas import CreateConversationSchema
from api.v1.Conversation.exceptions import ConversationNotFoundError


class ConversationService:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def create_conversation(self, data: CreateConversationSchema) -> Conversation:
        return self.repository.create(Conversation(**data.model_dump()))

    def get_conversation_by_id(self, conversation_id: int) -> Conversation:
        conversation = self.repository.get_by_id(conversation_id)
        if conversation is None:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
        return conversation


def get_conversation_service(
    repository: ConversationRepository = Depends(get_conversation_repository),
):
    return ConversationService(repository)
