from fastapi import Request, HTTPException
from app.services.cache_service import RedisService
from app.core.config import get_settings
import time

settings = get_settings()

async def rate_limit_middleware(request: Request, call_next):
    if request.method == "POST":
        client_ip = request.client.host
        redis_service = RedisService()
        rate_limit_key = f"rate_limit:{client_ip}:{int(time.time() / 60)}"

        if not await redis_service.check_rate_limit(rate_limit_key):
            raise HTTPException(
                status_code=429,
                detail="Too many requests. Please try again later."
            )

    response = await call_next(request)
    return response