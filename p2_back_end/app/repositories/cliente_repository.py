from sqlalchemy.orm import Session
from app.models.cliente import Cliente

class ClienteRepository:

    @staticmethod
    def listar(db: Session):
        return db.query(Cliente).all()

    @staticmethod
    def buscar_por_id(db: Session, id_cliente: int):
        return db.query(Cliente).filter(
            Cliente.id_cliente == id_cliente
        ).first()

    @staticmethod
    def criar(db: Session, cliente: Cliente):
        db.add(cliente)
        db.commit()
        db.refresh(cliente)
        return cliente

    @staticmethod
    def deletar(db: Session, cliente: Cliente):
        db.delete(cliente)
        db.commit()

    @staticmethod
    def atualizar(db: Session):
        db.commit()