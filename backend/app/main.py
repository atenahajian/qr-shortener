from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import urls
from app.core.config import get_settings

from app.core.logging import logger

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up application")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application")

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(urls.router, prefix=settings.API_V1_STR)
app.middleware("http")(rate_limit_middleware)