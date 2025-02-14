from sqlalchemy import Boolean, Column, String, DateTime, Float, ARRAY
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Node(Base):
    __tablename__ = "node"

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    is_active = Column(Boolean, default=True)
    text = Column(String, index=True)
    embedding = Column(ARRAY(Float), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())