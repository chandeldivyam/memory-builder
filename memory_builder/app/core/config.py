from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import validator
import json

class Settings(BaseSettings):
    PROJECT_NAME: str
    
    # Database
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str

    # Security
    SECRET_KEY: str

    # S3/MinIO
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_HOST: str
    MINIO_PORT: Optional[str] = '9000'
    MINIO_HOST_PORT: Optional[str] = None
    MINIO_HOST_CONSOLE_PORT: Optional[str] = None

    # Redis
    REDIS_HOST: str
    REDIS_PORT: str

    # Environment
    ENVIRONMENT: str = "development"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()