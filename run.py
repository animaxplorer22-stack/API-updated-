#!/usr/bin/env python3
import uvicorn
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app:create_app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        factory=True
    )
