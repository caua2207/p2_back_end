from pydantic import BaseModel
from decimal import Decimal

class PagamentoCreate(BaseModel):
    valor: Decimal
    forma_pagamento: str
    id_hospedagem: int