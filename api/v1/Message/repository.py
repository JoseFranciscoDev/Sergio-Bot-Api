from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.v1.Message.models import Message
from api.v1.shared.database import get_db


class MessageRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_messages_by_conversation(self, conversation_id: int) -> list[Message]:
        query = select(Message).where(Message.conversation_id == conversation_id)
        return list(self.session.execute(query).scalars().all())

    def create_message(self, new_message: Message) -> Message:
        try:
            self.session.add(new_message)
            self.session.commit()
            self.session.refresh(new_message)
            return new_message
        except Exception:
            self.session.rollback()
            raise


def get_message_repository(session: Session = Depends(get_db)):
    return MessageRepository(session)
