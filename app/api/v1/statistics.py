from fastapi import APIRouter, HTTPException
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/statistics", tags=["statistics"])

@router.get("/")
@cached(ttl_seconds=15)
async def get_statistics():
    result = await duco_client.get_statistics()
    if not result.get("success", False):
        raise HTTPException(status_code=503, detail="Could not fetch statistics")
    return result
