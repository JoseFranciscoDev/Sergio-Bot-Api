import enum
from datetime import datetime
from sqlalchemy import Text, Integer, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.v1.shared.base import Base


class MessageRole(enum.Enum):
    BOT = "bot"
    USER = "user"


class Message(Base):
    __tablename__ = "messages_table"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    conversation_id: Mapped[int] = mapped_column(
        Integer(), ForeignKey("conversations_table.id"), nullable=False
    )
    role: Mapped[MessageRole] = mapped_column(Enum(MessageRole), nullable=False)
    content: Mapped[str] = mapped_column(Text(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    conversation: Mapped["Conversation"] = relationship("Conversation", back_populates="messages")
