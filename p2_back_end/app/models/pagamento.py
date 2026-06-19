from sqlalchemy import Column, Integer, String, Numeric
from app.core.db import Base

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id_pagamento = Column(Integer, primary_key=True, index=True)
    valor = Column(Numeric(10,2), nullable=False)
    forma_pagamento = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)

    id_hospedagem = Column(Integer, nullable=False)