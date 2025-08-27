from fastapi import FastAPI
app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def index():
    return {"message": "Danfe smoke test is running."}
