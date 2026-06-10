from fastapi import HTTPException, Header
from typing import Optional
import hashlib
import secrets
from datetime import datetime, timedelta

_API_KEYS = {}

def generate_api_key(username: str) -> str:
    raw_key = f"duco_{secrets.token_urlsafe(32)}"
    key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
    _API_KEYS[key_hash] = {
        "username": username,
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(days=365)
    }
    return raw_key

def verify_api_key(api_key: str) -> str:
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()
    if key_hash not in _API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    key_data = _API_KEYS[key_hash]
    if key_data["expires_at"] < datetime.utcnow():
        del _API_KEYS[key_hash]
        raise HTTPException(status_code=401, detail="API key expired")
    return key_data["username"]

async def get_current_user(x_api_key: Optional[str] = Header(None)) -> Optional[str]:
    if x_api_key:
        return verify_api_key(x_api_key)
    return None
