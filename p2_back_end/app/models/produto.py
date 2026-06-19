from sqlalchemy import Column, Integer, String, Numeric
from app.core.db import Base

class Produto(Base):
    __tablename__ = "produtos"

    id_produto = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    valor = Column(Numeric(10,2), nullable=False)
    status = Column(String(20), nullable=False)