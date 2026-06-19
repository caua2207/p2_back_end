from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db

from app.models.compra import Compra
from app.models.produto import Produto

from app.schemas.compra import CompraCreate

from app.repositories.compra_repository import CompraRepository

router = APIRouter(
    prefix="/hospedagens",
    tags=["Hospedagens"]
)

@router.post("/")
def criar_compra(
    dados: CompraCreate,
    db: Session = Depends(get_db)
):

    produto = db.query(Produto).filter(
        Produto.id_produto == dados.id_produto
    ).first()

    if not produto:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "SUITE_NAO_ENCONTRADA",
        "mensagem": "Produto não encontrada",
        "detalhes": f"Produto {dados.id_produto} não existe"}
        )

    if produto.status != "Disponível":
        raise HTTPException(
            status_code=400,
            detail= {"codigo": "SUITE_NAO_DISPNIVEL",
        "mensagem": "Produto não está disponível",
        "detalhes": f"Produto {dados.id_produto} não está disponível"}
        )

    compra = Compra(
        data_compra=dados.data_compra,
        valor_total=0,
        id_cliente=dados.id_cliente,
        id_produto=dados.id_produto
    )

    produto.status = "fora de estoque"

    db.add(compra)
    db.commit()
    db.refresh(compra)

    return compra

@router.get("/")
def listar_compras(
    db: Session = Depends(get_db)
):
    return CompraRepository.listar(db)

@router.get("/{id_hospedagem}")
def buscar_Compra(
    id_compra: int,
    db: Session = Depends(get_db)
):
    compra = CompraRepository.buscar_por_id(
        db,
        id_compra
    )

    if not compra:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "Compra_NAO_ENCONTRADA",
        "mensagem": "Compra não encontrada",
        "detalhes": f"Compra {id_compra} não existe"}
        )

    return compra

@router.delete("/{id_compra}")
def deletar_compra(
    id_compra: int,
    db: Session = Depends(get_db)
):
    compra = CompraRepository.buscar_por_id(
        db,
        id_compra
    )

    if not compra:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "Compra_NAO_ENCONTRADA",
        "mensagem": "Compra não encontrada",
        "detalhes": f"Compra {id_compra} não existe"}
        )

    db.delete(compra)
    db.commit()

    return {
        "mensagem": "Compra removida com sucesso"
    }

