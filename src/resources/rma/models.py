# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database.database import Base

class RMA(Base):
    __tablename__ = 'rmas'

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'))  
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    status = Column(String, default='pendente')  
    motivo = Column(String, index=True)  
    data_solicitacao = Column(DateTime, default=datetime.utcnow)

    produto = relationship('Produto', back_populates='rmas')  
    usuario = relationship('Usuario', back_populates='rmas')  
