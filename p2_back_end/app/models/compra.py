from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.core.db import Base

class Compra(Base):
    __tablename__ = "hospedagens"

    id_hospedagem = Column(Integer, primary_key=True, index=True)
    data_entrada = Column(String(20), nullable=False)
    data_saida = Column(String(20))
    status = Column(String(20), nullable=False)
    valor_total = Column(Numeric(10,2), nullable=False)

    id_cliente = Column(
        Integer,
        ForeignKey("clientes.id_cliente"),
        nullable=False
    )

    id_produto = Column(
        Integer,
        ForeignKey("suites.id_suite"),
        nullable=False
    )