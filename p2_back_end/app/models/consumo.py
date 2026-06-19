from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.core.db import Base

class Consumo(Base):
    __tablename__ = "consumos"

    id_consumo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Numeric(10,2), nullable=False)

    id_hospedagem = Column(
        Integer,
        ForeignKey("hospedagens.id_hospedagem"),
        nullable=False
    )