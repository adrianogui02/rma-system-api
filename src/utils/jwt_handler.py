from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from src.config.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict) -> str:
    """
    Cria um token de acesso com uma data de expiração configurada.
    :param data: Dados para incluir no payload (geralmente, o ID do usuário).
    :return: Token JWT como string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "sub": str(data["sub"])})  # Adicionando o campo "sub" ao payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    """
    Verifica e decodifica o token JWT.
    :param token: Token JWT para validar.
    :return: Payload do token se válido, ou None se inválido.
    """
    try:
        # Tentando decodificar o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        # Captura qualquer erro e retorna um detalhe mais específico
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )