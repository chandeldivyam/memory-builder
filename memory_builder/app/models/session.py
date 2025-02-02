from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Session(Base):
    __tablename__ = "session"

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())