from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate
from app.repositories.produto_repository import ProdutoRepository

router = APIRouter(
    prefix="/suites",
    tags=["Suites"]
)

@router.post("/")
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    nova_produto = Produto(
        nome=produto.nome,
        valor=produto.valor,
        status=produto.status
    )

    return ProdutoRepository.criar(db, nova_produto)

@router.get("/")
def listar_produto(
    status: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Produto)

    if status:
        query = query.filter(
            Produto.status == status
        )


    return query.all()

@router.get("/{id_produto}")
def buscar_produto(
    id_produto: int,
    db: Session = Depends(get_db)
):
    produto = ProdutoRepository.buscar_por_id(
        db,
        id_produto
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "SUITE_NAO_ENCONTRADA",
        "mensagem": "Produto não encontrada",
        "detalhes": f"Produto {id_produto} não existe"}
        )

    return produto

@router.delete("/{id_suite}")
def deletar_produto(
    id_produto: int,
    db: Session = Depends(get_db)
):
    produto = ProdutoRepository.buscar_por_id(
        db,
        id_produto
    )

    if not produto:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "SUITE_NAO_ENCONTRADA",
        "mensagem": "Produto não encontrada",
        "detalhes": f"Produto {id_produto} não existe"}
        )

    ProdutoRepository.deletar(db, produto)

    return {
        "mensagem": "Produto removido com sucesso"
    }