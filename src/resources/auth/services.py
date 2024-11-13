from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from .models import Usuario
from .schema import UsuarioCreate, Token
from typing import Optional

# Configuração para criptografar senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Chave secreta para assinatura de JWT (defina uma chave forte no seu código real)
SECRET_KEY = "2e62f7d87d89aabb5a78b88f2548481be6e6fd9cc5c01bc22d9de6b489bfeb98"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Função para criptografar a senha
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar a senha
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Função para criar um token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Função para autenticar usuário
def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario and verify_password(senha, usuario.senha_hash):
        return usuario
    return None


# Função para criar novo usuário
def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nome=usuario.nome, 
        email=usuario.email, 
        senha_hash=hash_password(usuario.senha),
        role=usuario.role  # Definindo o papel do usuário
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

