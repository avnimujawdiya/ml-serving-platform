from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import get_current_user
from app.models.model import MLModel
from app.models.user import User
from app.schemas.model import ModelCreate, ModelResponse

router = APIRouter()

@router.post("/models", response_model=ModelResponse)
def register_model(
    payload: ModelCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_model = MLModel(**payload.dict())
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model
