from pydantic import BaseModel
from datetime import datetime

class Node(BaseModel):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
