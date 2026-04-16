from fastapi import FastAPI

app = FastAPI(title="CICD Test", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "cicd-test is running"}
