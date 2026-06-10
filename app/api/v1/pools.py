from fastapi import APIRouter
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/pools", tags=["pools"])

@router.get("/")
@cached(ttl_seconds=60)
async def get_pools():
    result = await duco_client.get_pools()
    if not result.get("success", False):
        return {"success": True, "result": []}
    return result

@router.get("/all")
@cached(ttl_seconds=60)
async def get_all_pools():
    result = await duco_client.get_pools()
    if not result.get("success", False):
        return {"success": True, "result": []}
    return result
