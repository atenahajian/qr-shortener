import logging
import sys
from pathlib import Path
from loguru import logger
from app.core.config import get_settings

settings = get_settings()

# Create logs directory
logs_path = Path("logs")
logs_path.mkdir(exist_ok=True)

# Configure loguru
logger.configure(
    handlers=[
        {
            "sink": sys.stdout,
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        },
        {
            "sink": "logs/app.log",
            "rotation": "500 MB",
            "retention": "10 days",
            "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        }
    ]
)