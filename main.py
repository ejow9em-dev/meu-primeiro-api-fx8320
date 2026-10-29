from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Meu FX 8320 tá on, pronto pra vaga remota"}

@app.get("/sobre")
def sobre():
    return {
        "nome": "Seu nome aqui",
        "objetivo": "Vaga remota backend",
        "stack": ["Python", "FastAPI"],
        "pc": "FX 8320"
    }

@app.get("/status")
def status():
    return {"status": "aprendendo e construindo portfólio todo dia"}
