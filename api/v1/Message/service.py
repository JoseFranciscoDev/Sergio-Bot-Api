from fastapi import Depends
from api.v1.Message.repository import MessageRepository, get_message_repository
from api.v1.Message.models import Message
from api.v1.Message.schemas import CreateMessageSchema
from api.v1.Conversation.repository import ConversationRepository, get_conversation_repository
from api.v1.Conversation.exceptions import ConversationNotFoundError


class MessageService:
    def __init__(self, repository: MessageRepository, conversation_repository: ConversationRepository):
        self.repository = repository
        self.conversation_repository = conversation_repository

    def create_message(self, data: CreateMessageSchema) -> Message:
        conversation = self.conversation_repository.get_by_id(data.conversation_id)
        if conversation is None:
            raise ConversationNotFoundError(f"Conversation {data.conversation_id} not found")
        return self.repository.create_message(Message(**data.model_dump()))

    def get_messages_by_conversation(self, conversation_id: int) -> list[Message]:
        conversation = self.conversation_repository.get_by_id(conversation_id)
        if conversation is None:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
        return self.repository.get_messages_by_conversation(conversation_id)


def get_message_service(
    repository: MessageRepository = Depends(get_message_repository),
    conversation_repository: ConversationRepository = Depends(get_conversation_repository),
):
    return MessageService(repository, conversation_repository)
