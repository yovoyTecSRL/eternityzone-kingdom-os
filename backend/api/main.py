from fastapi import FastAPI

app = FastAPI(title="EternityZone Kingdom OS API")

@app.get("/")
def root():
    return {"message": "Bienvenido al EternityZone Kingdom OS – API Online"}
