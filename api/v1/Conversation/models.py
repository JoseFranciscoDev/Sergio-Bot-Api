from datetime import datetime
from sqlalchemy import Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.v1.shared.base import Base


class Conversation(Base):
    __tablename__ = "conversations_table"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(), ForeignKey("users_table.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="conversation")
