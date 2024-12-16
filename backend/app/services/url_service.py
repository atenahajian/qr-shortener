import qrcode
import shortuuid
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.url import URL
from app.schemas.url import URLCreate
import os

class URLService:
    def __init__(self, db: Session):
        self.db = db
        self.qr_directory = "static/qr_codes"
        os.makedirs(self.qr_directory, exist_ok=True)

    def create_short_url(self, url_create: URLCreate) -> URL:
        # Generate unique short code
        short_code = shortuuid.uuid()[:8]
        
        # Create QR code
        qr_path = self._generate_qr_code(short_code, str(url_create.original_url))
        
        # Create URL record
        db_url = URL(
            original_url=str(url_create.original_url),
            short_code=short_code,
            qr_code_path=qr_path,
            expires_at=url_create.expires_at
        )
        
        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)
        
        return db_url

    def _generate_qr_code(self, short_code: str, url: str) -> str:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_path = f"{self.qr_directory}/{short_code}.png"
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_path)
        
        return qr_path

    def get_url_by_code(self, short_code: str) -> URL:
        url = self.db.query(URL).filter(URL.short_code == short_code).first()
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")
        return url

    def increment_click_count(self, url: URL):
        url.click_count += 1
        self.db.commit()
