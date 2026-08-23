from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from features.auth.services import authenticate_credentials
from shared.utils import format_response

# Buat Router khusus untuk fitur Auth
router = APIRouter(prefix="/auth", tags=["Authentication"])

# Schema untuk request body
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login_user(payload: LoginRequest):
    auth_result = authenticate_credentials(payload.username, payload.password)
    
    if auth_result["status"] == "success":
        return format_response(
            success=True, 
            message="Login berhasil!", 
            data={"user_id": auth_result["user_id"], "role": auth_result["role"]}
        )
    
    raise HTTPException(status_code=400, detail="Username atau password salah")