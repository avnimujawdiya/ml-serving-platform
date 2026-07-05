import time
import joblib
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import get_current_user
from app.core.rate_limiter import check_rate_limit
from app.models.model import MLModel
from app.models.prediction import Prediction
from app.models.user import User
from app.schemas.prediction import PredictRequest, PredictResponse

router = APIRouter()

@router.post("/predict/by-name/{model_name}", response_model=PredictResponse)
def predict_by_name(
    model_name: str,
    payload: PredictRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    _: None = Depends(check_rate_limit),
):
    model_record = db.query(MLModel).filter(
        MLModel.name == model_name,
        MLModel.status == "active"
    ).order_by(MLModel.created_at.desc()).first()

    if not model_record:
        raise HTTPException(status_code=404, detail="No active model found with that name")

    loaded_model = joblib.load(model_record.file_path)

    start = time.time()
    result = loaded_model.predict([payload.text])
    latency = (time.time() - start) * 1000

    log = Prediction(
        model_id=model_record.id,
        input_data={"text": payload.text},
        output_data={"prediction": int(result[0])},
        latency_ms=latency,
    )
    db.add(log)
    db.commit()

    return {"prediction": int(result[0]), "latency_ms": latency}
