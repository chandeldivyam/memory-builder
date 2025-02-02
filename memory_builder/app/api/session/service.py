from sqlalchemy.orm import Session as DBSession
from app.models.session import Session
import uuid
from datetime import datetime
from typing import Optional

class SessionService:
    def __init__(self, db: DBSession):
        self.db = db

    def create_session(self) -> Session:
        session = Session(
            id=str(uuid.uuid4()),
            is_active=True
        )
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        return self.db.query(Session).filter(Session.id == session_id).first()

    def deactivate_session(self, session_id: str) -> Optional[Session]:
        session = self.get_session(session_id)
        if session:
            session.is_active = False
            session.updated_at = datetime.utcnow()
            self.db.commit()
            self.db.refresh(session)
        return session 