from fastapi import FastAPI
from app.core.config import settings
import logging
from app.api.knowledge.router import router as knowledge_router
from app.api.session.router import router as session_router

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
)

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the memory builder"}

# Add this after your FastAPI app initialization
app.include_router(knowledge_router, prefix="/api/v1")
app.include_router(session_router, prefix="/api/v1")