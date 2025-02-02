from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.session import Session as SessionSchema
from app.api.session.service import SessionService
from typing import Optional

router = APIRouter(prefix="/session", tags=["session"])

@router.post("/", response_model=SessionSchema)
def create_session(
    db: Session = Depends(get_db)
):
    session_service = SessionService(db)
    return session_service.create_session()

@router.get("/{session_id}", response_model=SessionSchema)
def get_session(
    session_id: str,
    db: Session = Depends(get_db)
):
    session_service = SessionService(db)
    session = session_service.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.post("/{session_id}/deactivate", response_model=SessionSchema)
def deactivate_session(
    session_id: str,
    db: Session = Depends(get_db)
):
    session_service = SessionService(db)
    session = session_service.deactivate_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session 