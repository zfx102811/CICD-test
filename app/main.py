from fastapi import FastAPI

app = FastAPI(title="CICD Test")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "cicd-test is running"}
