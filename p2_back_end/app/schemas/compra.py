from pydantic import BaseModel
from decimal import Decimal

class CompraCreate(BaseModel):
    data_compra: str
    id_cliente: int
    id_suite: int
    
class CompraResponse(BaseModel):
    id_compra: int
    data_compra: str
    
    valor: Decimal
    id_cliente: int
    id_produto: int

    class Config:
        from_attributes = True