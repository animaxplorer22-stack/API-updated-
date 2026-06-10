import httpx
from typing import Optional, Dict, Any

class DUCOClient:
    def __init__(self):
        self.base_url = "https://server.duinocoin.com"
    
    async def _get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.get(f"{self.base_url}{endpoint}", params=params)
                if response.status_code == 200:
                    data = response.json()
                    if isinstance(data, dict) and "success" not in data:
                        return {"success": True, "result": data}
                    return data
                return {"success": False, "error": f"HTTP {response.status_code}"}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    async def get_user(self, username: str) -> Dict[str, Any]:
        return await self._get(f"/users/{username}")
    
    async def get_user_v2(self, username: str) -> Dict[str, Any]:
        return await self._get(f"/v2/users/{username}")
    
    async def get_miners(self, username: Optional[str] = None) -> Dict[str, Any]:
        if username:
            return await self._get(f"/miners/{username}")
        return await self._get("/miners")
    
    async def get_transactions(self, username: Optional[str] = None, limit: int = 10) -> Dict[str, Any]:
        params = {"limit": limit}
        if username:
            params["username"] = username
        return await self._get("/transactions", params=params)
    
    async def get_user_transactions(self, username: str, limit: int = 10) -> Dict[str, Any]:
        return await self._get(f"/user_transactions/{username}", params={"limit": limit})
    
    async def get_transaction_by_hash(self, hash_id: str) -> Dict[str, Any]:
        return await self._get(f"/transactions/{hash_id}")
    
    async def get_transaction_by_id(self, tx_id: int) -> Dict[str, Any]:
        return await self._get(f"/id_transactions/{tx_id}")
    
    async def get_balances(self, username: Optional[str] = None) -> Dict[str, Any]:
        if username:
            return await self._get(f"/balances/{username}")
        return await self._get("/balances")
    
    async def get_statistics(self) -> Dict[str, Any]:
        return await self._get("/statistics")
    
    async def get_pools(self) -> Dict[str, Any]:
        return await self._get("/all_pools")
    
    async def get_shop_items(self) -> Dict[str, Any]:
        return await self._get("/shop_items")
    
    async def check_mining_key(self, username: str, mining_key: str) -> Dict[str, Any]:
        return await self._get("/mining_key", params={"u": username, "k": mining_key})

duco_client = DUCOClient()
