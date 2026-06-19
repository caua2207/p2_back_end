from pydantic import BaseModel, field_validator

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    cpf: str
    email: str | None = None

    @field_validator("cpf")
    @classmethod
    def validar_cpf(cls, v):
        if not v.isdigit():
            raise ValueError("CPF deve conter apenas números")
        
        if len(v) != 11:
            raise ValueError("CPF deve possuir 11 dígitos")
        return v

class ClienteResponse(BaseModel):
    id_cliente: int
    nome: str
    telefone: str
    cpf: str
    email: str | None = None

    class Config:
        from_attributes = True