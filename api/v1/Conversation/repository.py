from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.v1.Conversation.models import Conversation
from api.v1.shared.database import get_db


class ConversationRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, conversation_id: int) -> Conversation | None:
        query = select(Conversation).where(Conversation.id == conversation_id)
        return self.session.execute(query).scalars().first()

    def create(self, new_conversation: Conversation) -> Conversation:
        try:
            self.session.add(new_conversation)
            self.session.commit()
            self.session.refresh(new_conversation)
            return new_conversation
        except Exception:
            self.session.rollback()
            raise


def get_conversation_repository(session: Session = Depends(get_db)):
    return ConversationRepository(session)
