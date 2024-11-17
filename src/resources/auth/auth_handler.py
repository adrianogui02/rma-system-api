from jose import JWTError, jwt
from src.config.config import SECRET_KEY, ALGORITHM

def decode_jwt(token: str) -> dict:
    try:
        # Decodifica o token e verifica sua validade
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
