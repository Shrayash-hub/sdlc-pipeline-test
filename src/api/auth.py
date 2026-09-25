from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["auth"])

class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest):
    # TODO: Add proper email validation
    # Currently accepts any string as email
    return {"message": "User registered", "email": request.email}