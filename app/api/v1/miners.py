from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/miners", tags=["miners"])

@router.get("/")
@cached(ttl_seconds=30)
async def get_all_miners(username: Optional[str] = Query(default=None)):
    result = await duco_client.get_miners(username)
    if not result.get("success", False):
        return {"success": True, "result": []}
    return result

@router.get("/{username}")
@cached(ttl_seconds=30)
async def get_user_miners(username: str):
    result = await duco_client.get_miners(username)
    if not result.get("success", False):
        return {"success": True, "result": []}
    return result

@router.get("/key/check")
async def check_mining_key(username: str = Query(...), mining_key: str = Query(...)):
    result = await duco_client.check_mining_key(username, mining_key)
    return result
