from datetime import datetime
from pydantic import BaseModel, ConfigDict
from api.v1.Message.models import MessageRole


class CreateMessageSchema(BaseModel):
    conversation_id: int
    role: MessageRole
    content: str


class MessageResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    conversation_id: int
    role: MessageRole
    content: str
    created_at: datetime
