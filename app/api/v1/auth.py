from fastapi import APIRouter, HTTPException
from app.services.duco_client import duco_client
from app.middleware.auth import generate_api_key
from app.models import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse, APIKeyRequest, APIKeyResponse

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=RegisterResponse)
async def register(request: RegisterRequest):
    success, message = await duco_client.register(request.username, request.password, request.email)
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return RegisterResponse(success=True, message=message)

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    success = await duco_client.login(request.username, request.password)
    if not success:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    api_key = generate_api_key(request.username)
    return LoginResponse(success=True, message="Login successful", token=api_key)

@router.post("/apikey", response_model=APIKeyResponse)
async def generate_new_apikey(request: APIKeyRequest):
    success = await duco_client.login(request.username, request.password)
    if not success:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    api_key = generate_api_key(request.username)
    return APIKeyResponse(success=True, api_key=api_key, message="API key generated successfully")
