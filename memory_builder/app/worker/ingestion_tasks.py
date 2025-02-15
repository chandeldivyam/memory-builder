import time
from app.core.celery_app import celery_app
from app.db.base import get_db
import logging
import traceback

logger = logging.getLogger(__name__)

@celery_app.task(
    name="process_ingestion_request",
    bind=True,
    max_retries=3,
    default_retry_delay=5
)
def process_ingestion_request(self, task_id: str, content: str):
    """
    Process knowledge ingestion task
    
    Args:
        task_id (str): Unique identifier for the task
        content (str): Content to be processed
    
    Returns:
        dict: Task result with status information
    """
    db = next(get_db())
    from app.memory.manager import get_memory_manager
    try:
        logger.info(f"Starting knowledge ingestion task {task_id}")
        # Here you would typically:
        # 1. Process the content (e.g., extract information, generate embeddings)
        # 2. Store the processed content
        # 3. Update any relevant indexes

        manager = get_memory_manager()

        logger.info(f"Ingesting content into memory manager")
        logger.info(f"Content Length: {len(content)}")
        manager.ingest(db = db, data = content)

        logger.info(f"Completed knowledge ingestion task {task_id}")
        return {
            "task_id": task_id,
            "status": "completed",
            "processed_length": len(content)
        }
    except Exception as e:
        traceback.print_exc()
        logger.error(f"Error processing task {task_id}: {str(e)}")
        self.retry(exc=e)
        return {
            "task_id": task_id,
            "status": "failed"
        }