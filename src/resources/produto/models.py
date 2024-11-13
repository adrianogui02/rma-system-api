import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database.database import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    descricao = Column(String)

    rmas = relationship('RMA', back_populates='produto')  # Relacionamento com RMA