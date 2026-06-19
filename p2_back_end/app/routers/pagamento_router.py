from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db

from app.models.pagamento import Pagamento
from app.models.compra import Compra

from app.schemas.pagamento import PagamentoCreate

router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamentos"]
)

@router.post("/")
def criar_pagamento(
    dados: PagamentoCreate,
    db: Session = Depends(get_db)
):

    if dados.valor <= 0:
        raise HTTPException(
            status_code=400,
            detail= {"codigo": "VALOR_INVALIDO",
        "mensagem": "Valor inválido",
        "detalhes": "O valor do pagamento deve ser positivo"}
        )

    compra = db.query(Compra).filter(
        Compra.id_compra == dados.id_compra
    ).first()

    if not compra:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "Compra_NAO_ENCONTRADA",
        "mensagem": "Compra não encontrada",
        "detalhes": f"COmpra {dados.id_compra} não existe"}
        )

    if compra.status != "Finalizada":
        raise HTTPException(
            status_code=400,
            detail= {"codigo": "Compra_NAO_FINALIZADA",
        "mensagem": "A compra deve estar finalizada para receber pagamento",
        "detalhes": f"Compra {dados.id_compra} não está finalizada"}
        )

    pagamento = Pagamento(
        valor=dados.valor,
        forma_pagamento=dados.forma_pagamento,
        status="Confirmado",
        id_hospedagem=dados.id_hospedagem
    )

    db.add(pagamento)
    db.commit()
    db.refresh(pagamento)

    return pagamento

@router.get("/")
def listar_pagamentos(
    db: Session = Depends(get_db)
):
    return db.query(Pagamento).all()

@router.get("/{id_pagamento}")
def buscar_pagamento(
    id_pagamento: int,
    db: Session = Depends(get_db)
):
    pagamento = db.query(Pagamento).filter(
        Pagamento.id_pagamento == id_pagamento
    ).first()

    if not pagamento:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "PAGAMENTO_NAO_ENCONTRADO",
        "mensagem": "Pagamento não encontrado",
        "detalhes": f"Pagamento {id_pagamento} não existe"}
        )

    return pagamento