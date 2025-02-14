from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from .node import Node

class Query(BaseModel):
    text: str

class QueryResponse(BaseModel):
    results: list[Optional[Node]]
