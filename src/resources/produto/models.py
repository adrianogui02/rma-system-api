from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from src.database.database import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    descricao = Column(String)
    usuario_id = Column(String, ForeignKey('usuarios.id'))  # Adiciona o campo de chave estrangeira

    # Estabelece o relacionamento com a tabela de 'usuarios'
    usuario = relationship('Usuario', back_populates='produtos')

    rmas = relationship('RMA', back_populates='produto')  # Relacionamento com RMA
