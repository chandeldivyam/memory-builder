from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from .node import Node
from typing import List

class Query(BaseModel):
    text: str

class QueryResult(BaseModel):
    node: Optional[Node]
    distance: float

class QueryResponse(BaseModel):
    results: List[QueryResult]
