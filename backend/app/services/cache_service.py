import redis
from app.core.config import get_settings
from typing import Optional

settings = get_settings()

class RedisService:
    def __init__(self):
        self.redis_client = redis.from_url(settings.REDIS_URL)
        self.default_expiry = 3600  # 1 hour

    async def set_cache(self, key: str, value: str, expiry: int = None) -> None:
        """Set a key-value pair in Redis cache"""
        await self.redis_client.set(
            key,
            value,
            ex=expiry if expiry is not None else self.default_expiry
        )

    async def get_cache(self, key: str) -> Optional[str]:
        """Get a value from Redis cache by key"""
        value = await self.redis_client.get(key)
        return value.decode('utf-8') if value else None

    async def delete_cache(self, key: str) -> None:
        """Delete a key from Redis cache"""
        await self.redis_client.delete(key)

    async def increment_counter(self, key: str) -> int:
        """Increment a counter in Redis"""
        return await self.redis_client.incr(key)

    async def check_rate_limit(self, key: str) -> bool:
        """Check if rate limit is exceeded"""
        count = await self.increment_counter(key)
        if count == 1:
            await self.redis_client.expire(key, 60)  # 1 minute window
        return count <= settings.RATE_LIMIT_PER_MINUTE