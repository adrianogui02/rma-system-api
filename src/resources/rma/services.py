# services.py
from sqlalchemy.orm import Session
from .models import RMA
from .schema import RMABase, RMAUpdate

# Função para criar um novo RMA
def criar_rma(db: Session, rma: RMABase, usuario_id: str) -> RMA:
    db_rma = RMA(produto_id=rma.produto_id, motivo=rma.motivo, usuario_id=usuario_id)
    db.add(db_rma)
    db.commit()
    db.refresh(db_rma)
    return db_rma

# Função para atualizar o status de um RMA
def atualizar_rma_status(db: Session, rma_id: str, status: str) -> RMA:
    db_rma = db.query(RMA).filter(RMA.id == rma_id).first()
    if db_rma:
        db_rma.status = status
        db.commit()
        db.refresh(db_rma)
        return db_rma
    return None

# Função para obter todos os RMAs de um usuário
def obter_rmas_usuario(db: Session, usuario_id: str):
    return db.query(RMA).filter(RMA.usuario_id == usuario_id).all()
