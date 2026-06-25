from fastapi import FastAPI, Depends
from app.core.security import get_current_user
from app.models.user import User
from app.api.models import router as models_router

app = FastAPI(title="ML Serving Platform")

app.include_router(models_router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email}
