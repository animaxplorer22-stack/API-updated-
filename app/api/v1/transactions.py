from fastapi import APIRouter, HTTPException, Query
from app.services.duco_client import duco_client
from app.cache import cached

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("/")
@cached(ttl_seconds=30)
async def get_transactions(username: str = Query(None), limit: int = Query(10, ge=1, le=100)):
    if username:
        result = await duco_client.get_user_transactions(username, limit)
    else:
        result = await duco_client.get_transactions(limit=limit)
    
    if not result.get("success", False):
        return {"success": True, "result": {}}
    return result

@router.get("/{hash_id}")
@cached(ttl_seconds=60)
async def get_transaction_by_hash(hash_id: str):
    result = await duco_client.get_transaction_by_hash(hash_id)
    if not result.get("success", False):
        raise HTTPException(status_code=404, detail="Transaction not found")
    return result

@router.get("/id/{tx_id}")
@cached(ttl_seconds=60)
async def get_transaction_by_id(tx_id: int):
    result = await duco_client.get_transaction_by_id(tx_id)
    if not result.get("success", False):
        raise HTTPException(status_code=404, detail="Transaction not found")
    return result

@router.get("/user/{username}")
@cached(ttl_seconds=30)
async def get_user_transactions(username: str, limit: int = Query(10, ge=1, le=100)):
    result = await duco_client.get_user_transactions(username, limit)
    if not result.get("success", False):
        return {"success": True, "result": {username: []}}
    return result
