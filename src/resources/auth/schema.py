from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    nome: str
    email: str
    role: Optional[str] = "user" 

class LoginRequest(BaseModel):
    email: str
    senha: str 

class UserCreate(UserBase):
    senha: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int
    email: str
    role: str  

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    role: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
