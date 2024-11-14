from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError
from .schema import UserCreate, Token, LoginRequest, LoginResponse
from .services import criar_usuario, autenticar_usuario, create_access_token
from src.database.database import SessionLocal
from datetime import timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=Token)
def register(usuario: UserCreate, db: Session = Depends(get_db)):
    db_usuario = criar_usuario(db, usuario)
    access_token = create_access_token(data={"sub": db_usuario.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, request.email, request.senha)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": usuario.email, "role": usuario.role})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "role": usuario.role
        }
    }



