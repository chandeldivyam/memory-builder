from pydantic import BaseModel
from datetime import datetime
from typing import List

class Node(BaseModel):
    id: str
    is_active: bool
    text: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_orm(cls, orm_obj):
        return cls(
            id=orm_obj.id,
            is_active=orm_obj.is_active,
            text=orm_obj.text,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at
        )