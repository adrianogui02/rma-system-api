from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nome: str
    email: str
    role: Optional[str] = "user" 

class LoginRequest(BaseModel):
    email: str
    senha: str 

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str
    email: str
    role: str  

class UserResponse(BaseModel):
    id: str
    nome: str
    email: str
    role: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
