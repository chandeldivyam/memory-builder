from fastapi import APIRouter, HTTPException, Depends
from app.db.base import get_db
from sqlalchemy.orm import Session
from app.worker.ingestion_tasks import process_ingestion_request
from typing import Optional
from app.schemas.knowledge import KnowledgeIngest, KnowledgeIngestResponse
# logging
import logging
import uuid

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.post("/ingest", response_model=KnowledgeIngestResponse)
async def ingest_knowledge(content: KnowledgeIngest, db: Session = Depends(get_db)):
    """
    Ingest knowledge content and process it asynchronously
    """
    try:
        # Generate a task ID
        task_id = str(uuid.uuid4())
        
        # Start celery task with both required parameters
        task = process_ingestion_request.delay(db, task_id, content.content)
        
        # Update the task ID to use Celery's task ID for consistency
        return {"task_id": task.id, "status": "processing"}
    except Exception as e:
        logger.error(f"Error starting knowledge ingestion task: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to start knowledge ingestion")

@router.get("/task_status/{task_id}", response_model=KnowledgeIngestResponse)
async def get_task_status(task_id: str):
    """
    Get the status of a knowledge ingestion task
    """
    task = process_ingestion_request.AsyncResult(task_id)
    
    # Map Celery states to our status format
    if task.state == 'PENDING':
        status = "pending"
    elif task.state == 'STARTED':
        status = "processing"
    elif task.state == 'SUCCESS':
        status = "completed"
    elif task.state == 'FAILURE':
        status = "failed"
    else:
        status = task.state.lower()
    
    return {"task_id": task_id, "status": status}
