from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/balances", tags=["balances"])

@router.get("/")
@cached(ttl_seconds=60)
async def get_all_balances(limit: int = Query(100, ge=1, le=500)):
    result = await duco_client.get_balances()
    if not result.get("success", False):
        raise HTTPException(status_code=503, detail="Could not fetch balances")
    if "result" in result and isinstance(result["result"], list):
        result["result"] = result["result"][:limit]
    return result

@router.get("/{username}")
@cached(ttl_seconds=30)
async def get_user_balance(username: str):
    result = await duco_client.get_balances(username)
    if not result.get("success", False):
        raise HTTPException(status_code=404, detail="User not found")
    return result
