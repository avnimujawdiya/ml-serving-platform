from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.session import get_db
from app.core.security import get_current_user
from app.models.prediction import Prediction
from app.models.user import User
from app.schemas.prediction_list import PredictionOut

router = APIRouter()

@router.get("/predictions", response_model=List[PredictionOut])
def list_predictions(
    model_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Prediction)
    if model_id is not None:
        query = query.filter(Prediction.model_id == model_id)
    return query.order_by(Prediction.created_at.desc()).all()
