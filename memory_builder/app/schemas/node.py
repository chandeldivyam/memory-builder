from pydantic import BaseModel
from datetime import datetime

class Node(BaseModel):
    id: str
    is_active: bool
    text: str
    embedding: list
    created_at: datetime
    updated_at: datetime
