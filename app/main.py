from fastapi import FastAPI

app = FastAPI(title="ML Serving Platform")

@app.get("/health")
def health():
    return {"status": "ok"}
