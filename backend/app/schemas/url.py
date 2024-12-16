from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class URLBase(BaseModel):
    original_url: HttpUrl

class URLCreate(URLBase):
    expires_at: Optional[datetime] = None

class URLResponse(URLBase):
    id: int
    short_code: str
    qr_code_path: Optional[str]
    created_at: datetime
    expires_at: Optional[datetime]
    click_count: int

    class Config:
        from_attributes = True
