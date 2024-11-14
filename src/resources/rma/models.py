# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from src.database.database import Base

class RMA(Base):
    __tablename__ = 'rmas'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    produto_id = Column(String, ForeignKey('produtos.id'))  
    usuario_id = Column(String, ForeignKey('usuarios.id'))
    status = Column(String, default='pendente')  
    motivo = Column(String, index=True)  
    data_solicitacao = Column(DateTime, default=datetime.utcnow)

    produto = relationship('Produto', back_populates='rmas')  
    usuario = relationship('Usuario', back_populates='rmas')  
