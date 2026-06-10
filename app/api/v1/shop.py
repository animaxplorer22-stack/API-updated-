from fastapi import APIRouter, HTTPException
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/shop", tags=["shop"])

@router.get("/items")
@cached(ttl_seconds=300)
async def get_shop_items():
    result = await duco_client.get_shop_items()
    if not result.get("success", False):
        return {"success": True, "result": {}}
    return result
