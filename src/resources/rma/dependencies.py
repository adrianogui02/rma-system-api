# dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.config.config import SECRET_KEY, ALGORITHM
from src.resources.auth.models import Usuario

# Definindo o OAuth2PasswordBearer para capturar o token do cabeçalho Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_user_id(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
