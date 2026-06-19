from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db

from app.models.consumo import Consumo
from app.models.compra import Hospedagem

from app.schemas.consumo import ConsumoCreate

router = APIRouter(
    prefix="/consumos",
    tags=["Consumos"]
)

@router.post("/")
def criar_consumo(
    dados: ConsumoCreate,
    db: Session = Depends(get_db)
):

    hospedagem = db.query(Hospedagem).filter(
        Hospedagem.id_hospedagem == dados.id_hospedagem
    ).first()

    if not hospedagem:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "HOSPEDAGEM_NAO_ENCONTRADA",
        "mensagem": "Hospedagem não encontrada",
        "detalhes": f"Hospedagem {dados.id_hospedagem} não existe"}
        )

    if hospedagem.status != "Em Andamento":
        raise HTTPException(
            status_code=400,
            detail= {"codigo": "HOSPEDAGEM_ENCERRADA",
        "mensagem": "Hospedagem encerrada",
        "detalhes": f"Hospedagem {dados.id_hospedagem} está encerrada"}
        )

    consumo = Consumo(
        descricao=dados.descricao,
        quantidade=dados.quantidade,
        valor_unitario=dados.valor_unitario,
        id_hospedagem=dados.id_hospedagem
    )

    db.add(consumo)

    hospedagem.valor_total += (
        dados.quantidade * dados.valor_unitario
    )

    db.commit()

    return consumo
@router.get("/")
def listar_consumos(
    db: Session = Depends(get_db)
):
    return db.query(Consumo).all()

@router.get("/{id_consumo}")
def buscar_consumo(
    id_consumo: int,
    db: Session = Depends(get_db)
):
    consumo = db.query(Consumo).filter(
        Consumo.id_consumo == id_consumo
    ).first()

    if not consumo:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "CONSUMO_NAO_ENCONTRADO",
        "mensagem": "Consumo não encontrado",
        "detalhes": f"Consumo {id_consumo} não existe"}
        )

    return consumo

@router.delete("/{id_consumo}")
def deletar_consumo(
    id_consumo: int,
    db: Session = Depends(get_db)
):
    consumo = db.query(Consumo).filter(
        Consumo.id_consumo == id_consumo
    ).first()

    if not consumo:
        raise HTTPException(
            status_code=404,
            detail= {"codigo": "CONSUMO_NAO_ENCONTRADO",
        "mensagem": "Consumo não encontrado",
        "detalhes": f"Consumo {id_consumo} não existe"}
        )

    db.delete(consumo)
    db.commit()

    return {
        "mensagem": "Consumo removido com sucesso"
    }