from sqlalchemy.orm import Session
from app.models.produto import Produto

class SuiteRepository:

    @staticmethod
    def criar(db: Session, produto: Produto):
        db.add(produto)
        db.commit()
        db.refresh(produto)
        return produto

    @staticmethod
    def listar(db: Session):
        return db.query(Produto).all()

    @staticmethod
    def buscar_por_id(db: Session, id_produto: int):
        return db.query(Produto).filter(
            Produto.id_produto == id_produto
        ).first()

    @staticmethod
    def deletar(db: Session, produto: Produto):
        db.delete(produto)
        db.commit()