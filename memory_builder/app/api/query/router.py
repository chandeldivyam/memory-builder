from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.query import Query, QueryResponse
from app.api.query.service import QueryService
from typing import Optional, List

router = APIRouter(prefix="/query", tags=["node"])

@router.post("/", response_model=QueryResponse)
async def get_nodes(query: Query, query_service: QueryService = Depends(), db: Session = Depends(get_db)):
    return query_service.get_nodes(db, query.text)
