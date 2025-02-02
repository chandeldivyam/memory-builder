from pydantic import BaseModel
from typing import List

class KnowledgeIngest(BaseModel):
    content: str
    tags: List[str]

class KnowledgeIngestResponse(BaseModel):
    status: str
    task_id: str
