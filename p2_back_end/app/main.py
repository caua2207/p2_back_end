from fastapi import FastAPI
from app.core.db import Base, engine
from app.models.cliente import Cliente
from app.models.produto import Produto
from app.models.compra import Compra
from app.models.consumo import Consumo
from app.models.pagamento import Pagamento
from app.routers.cliente_router import router as cliente_router
from app.routers.produto_router import router as produto_router
from app.routers.compra_router import router as compra_router
from app.routers.consumo_router import router as consumo_router
from app.routers.pagamento_router import router as pagamento_router




# Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Sistema de Motel",
    version="1.0.0"
)
app.include_router(cliente_router)
app.include_router(produto_router)
app.include_router(compra_router)
app.include_router(consumo_router)
app.include_router(pagamento_router)


@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}