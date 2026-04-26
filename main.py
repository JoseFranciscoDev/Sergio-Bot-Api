from fastapi import FastAPI
from api.v1.routers import router as v1_router
from api.v1.shared.database import init_db

app = FastAPI()
app.include_router(v1_router)
init_db()


@app.get("/status")
def status() -> dict[str, str]:
    return {"status": "Olha, funciono"}

"""
A api precisa gerir transacoes:
Adicionar saldo;
remover saldo;
Precisamos também gerir usuários, o que inclue:
Criar usuário;
Remover;
Editar;
A api também precisa  de capacidade de conversar com a api do gemini

"""