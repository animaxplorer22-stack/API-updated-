from functools import wraps
from datetime import datetime, timedelta
from app.config import settings

_in_memory_cache = {}

def cached(ttl_seconds: int = 60):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            current_time = datetime.utcnow()
            
            if cache_key in _in_memory_cache:
                cached_time, cached_value = _in_memory_cache[cache_key]
                if current_time - cached_time < timedelta(seconds=ttl_seconds):
                    return cached_value
            
            result = await func(*args, **kwargs)
            _in_memory_cache[cache_key] = (current_time, result)
            return result
        return wrapper
    return decorator

def clear_cache():
    _in_memory_cache.clear()
