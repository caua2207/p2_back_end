from pydantic import BaseModel
from decimal import Decimal

class CompraCreate(BaseModel):
    numero: int
    nome: str
    categoria: str
    valor_hora: Decimal
    status: str

class ProdutoResponse(BaseModel):
    id_produto: int
    nome: str
    valor: Decimal
    status: str

    class Config:
        from_attributes = True