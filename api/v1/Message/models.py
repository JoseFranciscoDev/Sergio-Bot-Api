import enum
from sqlalchemy import Text, Integer, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from api.v1.shared.base import Base


class MessageRole(enum.Enum):
    BOT = "bot"
    USER = "user"


class Message(Base):
    __tablename__ = "message_table"

    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer(),
        ForeignKey("users_table.id"),
        nullable=False,
    )
    role: Mapped[MessageRole] = mapped_column(
        Enum(MessageRole),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text(),
        nullable=False,
    )
