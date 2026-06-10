from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import users, miners, transactions, statistics, auth, balances, shop, pools, websocket
from app.middleware.rate_limit import RateLimitMiddleware
from app.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description="Public REST API for Duino-Coin",
        version="2.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.add_middleware(RateLimitMiddleware)
    
    app.include_router(users.router, prefix="/api/v1")
    app.include_router(miners.router, prefix="/api/v1")
    app.include_router(transactions.router, prefix="/api/v1")
    app.include_router(statistics.router, prefix="/api/v1")
    app.include_router(auth.router, prefix="/api/v1")
    app.include_router(balances.router, prefix="/api/v1")
    app.include_router(shop.router, prefix="/api/v1")
    app.include_router(pools.router, prefix="/api/v1")
    app.include_router(websocket.router, prefix="/api/v1")
    
    @app.get("/")
    async def root():
        return {
            "name": settings.APP_NAME,
            "version": "2.0.0",
            "docs": "/docs",
            "endpoints": [
                "/api/v1/users/{username}",
                "/api/v1/miners/{username}",
                "/api/v1/transactions/user/{username}",
                "/api/v1/statistics",
                "/api/v1/auth/register",
                "/api/v1/auth/login",
                "/api/v1/balances/{username}",
                "/api/v1/shop/items",
                "/api/v1/pools/all"
            ]
        }
    
    return app
