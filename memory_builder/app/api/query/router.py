from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.query import Query, QueryResponse
from app.api.query.service import NodeService
from typing import Optional, List

router = APIRouter(prefix="/query", tags=["node"])

@router.get("/", response_model=QueryResponse)
async def get_nodes(query: Query, node_service: NodeService = Depends(), db: Session = Depends(get_db)):
    return node_service.get_nodes(db, query.text)
