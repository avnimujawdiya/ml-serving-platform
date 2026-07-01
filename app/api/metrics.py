from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.core.security import get_current_user
from app.models.model import MLModel
from app.models.prediction import Prediction
from app.models.user import User

router = APIRouter()

@router.get("/models/{model_id}/metrics")
def get_model_metrics(
    model_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    model_record = db.query(MLModel).filter(MLModel.id == model_id).first()
    if not model_record:
        raise HTTPException(status_code=404, detail="Model not found")

    total = db.query(func.count(Prediction.id))\
        .filter(Prediction.model_id == model_id)\
        .scalar()

    avg_latency = db.query(func.avg(Prediction.latency_ms))\
        .filter(Prediction.model_id == model_id)\
        .scalar()

    return {
        "model_id": model_id,
        "model_name": model_record.name,
        "version": model_record.version,
        "total_predictions": total,
        "avg_latency_ms": round(avg_latency, 4) if avg_latency else None,
    }
