from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Meu FX 8320 tá on, pronto pra vaga remota"}
