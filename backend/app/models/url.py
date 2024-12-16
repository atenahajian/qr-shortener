from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False, index=True)
    qr_code_path = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, default=True)
    click_count = Column(Integer, default=0)

class Click(Base):
    __tablename__ = "clicks"
    
    id = Column(Integer, primary_key=True, index=True)
    url_id = Column(Integer, ForeignKey("urls.id"))
    clicked_at = Column(DateTime(timezone=True), server_default=func.now())
    ip_address = Column(String)
    user_agent = Column(String)
    referrer = Column(String, nullable=True)