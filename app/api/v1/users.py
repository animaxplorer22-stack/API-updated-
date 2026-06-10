from fastapi import APIRouter, HTTPException
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{username}")
@cached(ttl_seconds=30)
async def get_user(username: str):
    result = await duco_client.get_user(username)
    if not result.get("success", False):
        raise HTTPException(status_code=404, detail="User not found")
    return result

@router.get("/v2/{username}")
@cached(ttl_seconds=30)
async def get_user_v2(username: str):
    result = await duco_client.get_user_v2(username)
    if not result.get("success", False):
        raise HTTPException(status_code=404, detail="User not found")
    return result
