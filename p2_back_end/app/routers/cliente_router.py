from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate
from app.repositories.cliente_repository import ClienteRepository
from fastapi import HTTPException


router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.get("/")
def listar_clientes(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return db.query(Cliente)\
        .offset(offset)\
        .limit(limit)\
        .all()

        
@router.post("/")
def criar_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    novo_cliente = Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        cpf=cliente.cpf
    )

    return ClienteRepository.criar(
        db,
        novo_cliente
    )

@router.get("/{id_cliente}")
def buscar_cliente(
    id_cliente: int,
    db: Session = Depends(get_db)
):
    cliente = ClienteRepository.buscar_por_id(
        db,
        id_cliente
    )

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "CLIENTE_NAO_ENCONTRADO",
        "mensagem": "Cliente não encontrado",
        "detalhes": f"Cliente {id_cliente} não existe"}
        )

    return cliente

@router.delete("/{id_cliente}")
def deletar_cliente(
    id_cliente: int,
    db: Session = Depends(get_db)
):
    cliente = ClienteRepository.buscar_por_id(
        db,
        id_cliente
    )

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "CLIENTE_NAO_ENCONTRADO",
        "mensagem": "Cliente não encontrado",
        "detalhes": f"Cliente {id_cliente} não existe"}
        )

    ClienteRepository.deletar(db, cliente)

    return {
        "mensagem": "Cliente removido com sucesso"
    }

@router.put("/{id_cliente}")
def atualizar_cliente(
    id_cliente: int,
    dados: ClienteCreate,
    db: Session = Depends(get_db)
):
    cliente = ClienteRepository.buscar_por_id(
        db,
        id_cliente
    )

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "CLIENTE_NAO_ENCONTRADO",
        "mensagem": "Cliente não encontrado",
        "detalhes": f"Cliente {id_cliente} não existe"}
        )

    cliente.nome = dados.nome
    cliente.telefone = dados.telefone
    cliente.cpf = dados.cpf
    cliente.email = dados.email

    db.commit()
    db.refresh(cliente)

    return cliente