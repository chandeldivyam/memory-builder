from sqlalchemy import Boolean, Column, String, DateTime, Float
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from app.db.base import Base
import uuid

N_DIM = 3072

class Node(Base):
    __tablename__ = "node"

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    is_active = Column(Boolean, default=True)
    text = Column(String, index=True)
    embedding = Column(Vector(N_DIM))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())