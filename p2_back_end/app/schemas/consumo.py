from pydantic import BaseModel
from decimal import Decimal

class ConsumoCreate(BaseModel):
    descricao: str
    quantidade: int
    valor_unitario: Decimal
    id_hospedagem: int