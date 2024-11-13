from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    role = Column(String, default="user")  # role pode ser 'admin' ou 'user'
    rmas = relationship('RMA', back_populates='usuario')  # Relacionamento com RMA
