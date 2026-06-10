from pydantic_settings import BaseSettings
import warnings

class Settings(BaseSettings):
    APP_NAME: str = "DUCO Public API"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    DUCO_SERVER_HOST: str = "51.15.127.80"
    DUCO_SERVER_PORT: int = 2811
    DUCO_SERVER_WS: str = "ws://51.15.127.80:15808"
    
    SECRET_KEY: str = ""
    JWT_EXPIRATION_MINUTES: int = 60
    JWT_ALGORITHM: str = "HS256"
    
    RATE_LIMIT_PER_MINUTE: int = 60
    RATE_LIMIT_PER_DAY: int = 10000
    
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_ENABLED: bool = False
    
    class Config:
        env_file = ".env"
        extra = "ignore"
    
    def get_secret_key(self) -> str:
        if not self.SECRET_KEY or self.SECRET_KEY == "replace_with_your_32_byte_hex_secret_key":
            warnings.warn("SECRET_KEY not set in .env file", RuntimeWarning)
            return "temporary_secret_key_for_development"
        return self.SECRET_KEY

settings = Settings()
