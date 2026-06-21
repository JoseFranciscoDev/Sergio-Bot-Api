from datetime import datetime
from pydantic import BaseModel, ConfigDict


class CreateConversationSchema(BaseModel):
    user_id: int


class ConversationResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: datetime
