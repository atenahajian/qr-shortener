# app/api/endpoints/urls.py
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.url import URLCreate, URLResponse
from app.services.url_service import URLService
from app.core.config import get_settings
from fastapi.responses import RedirectResponse
from typing import List

router = APIRouter()
settings = get_settings()

@router.post("/shorten", response_model=URLResponse)
def create_short_url(
    url_create: URLCreate,
    db: Session = Depends(get_db)
):
    url_service = URLService(db)
    return url_service.create_short_url(url_create)

@router.get("/{short_code}")
def redirect_to_url(
    short_code: str,
    request: Request,
    db: Session = Depends(get_db)
):
    url_service = URLService(db)
    url = url_service.get_url_by_code(short_code)
    url_service.increment_click_count(url)
    
    return RedirectResponse(url.original_url)

@router.get("/url/{short_code}", response_model=URLResponse)
def get_url_info(
    short_code: str,
    db: Session = Depends(get_db)
):
    url_service = URLService(db)
    return url_service.get_url_by_code(short_code)