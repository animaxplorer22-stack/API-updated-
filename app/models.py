from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from datetime import datetime

class UserResponse(BaseModel):
    success: bool
    result: Dict[str, Any]

class MinerStats(BaseModel):
    accepted: int
    algorithm: str
    diff: int
    hashrate: float
    identifier: str
    rejected: int
    sharetime: float
    software: str
    username: str

class MinersResponse(BaseModel):
    success: bool
    result: List[MinerStats]

class Transaction(BaseModel):
    amount: float
    datetime: str
    hash: str
    memo: str
    recipient: str
    sender: str
    id: int

class TransactionsResponse(BaseModel):
    success: bool
    result: Dict[str, List[Transaction]]

class StatisticsResponse(BaseModel):
    success: bool
    result: Dict[str, Any]

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    password: str = Field(..., min_length=6, max_length=128)
    email: str

    @validator('username')
    def username_valid(cls, v):
        if not v[0].isalpha():
            raise ValueError('Username must start with a letter')
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username can only contain letters, numbers, underscores, and hyphens')
        return v.lower()

class RegisterResponse(BaseModel):
    success: bool
    message: str

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str
    token: Optional[str] = None

class APIKeyRequest(BaseModel):
    username: str
    password: str

class APIKeyResponse(BaseModel):
    success: bool
    api_key: str
    message: str
