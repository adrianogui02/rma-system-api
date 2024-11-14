from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .services import criar_rma, atualizar_rma_status, obter_rmas_usuario
from .schema import RMABase, RMAUpdate, RMA
from src.database.database import SessionLocal
from src.resources.auth.auth_bearer import JWTBearer

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar um RMA
@router.post("/rmas", response_model=RMA)
def criar_rma_view(rma: RMABase, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    # O token foi validado, agora você pode acessar a lógica de criação do RMA
    db_rma = criar_rma(db, rma, token)
    return db_rma

# Atualizar status de um RMA
@router.put("/rmas/{rma_id}", response_model=RMA)
def atualizar_rma_status_view(rma_id: str, rma_update: RMAUpdate, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    db_rma = atualizar_rma_status(db, rma_id, rma_update.status)
    if db_rma is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RMA not found")
    return db_rma

# Obter RMAs de um usuário
@router.get("/rmas", response_model=list[RMA])
def obter_rmas_view(db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    # O token foi validado, agora você pode acessar a lógica de obter RMAs
    rmas = obter_rmas_usuario(db, token)
    return rmas