from pydantic import BaseModel
from datetime import datetime

class Session(BaseModel):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: datetime