from sqlalchemy.orm import Session
from app.models.compra import Compra

class CompraRepository:

    @staticmethod
    def criar(db: Session, compra: Compra):
        db.add(compra)
        db.commit()
        db.refresh(compra)
        return compra

    @staticmethod
    def listar(db: Session):
        return db.query(Compra).all()

    @staticmethod
    def buscar_por_id(db: Session, id_compra: int):
        return db.query(Compra).filter(
            Compra.id_compra == id_compra
        ).first()