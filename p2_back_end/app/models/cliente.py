from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(15), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    email = Column(String(100), nullable=True)