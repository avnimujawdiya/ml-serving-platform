import time
import joblib
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import get_current_user
from app.models.model import MLModel
from app.models.prediction import Prediction
from app.models.user import User
from app.schemas.prediction import PredictRequest, PredictResponse

router = APIRouter()

@router.post("/predict/{model_id}", response_model=PredictResponse)
def predict(
    model_id: int,
    payload: PredictRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    model_record = db.query(MLModel).filter(MLModel.id == model_id).first()
    if not model_record:
        raise HTTPException(status_code=404, detail="Model not found")

    loaded_model = joblib.load(model_record.file_path)

    start = time.time()
    result = loaded_model.predict([payload.text])
    latency = (time.time() - start) * 1000

    log = Prediction(
        model_id=model_id,
        input_data={"text": payload.text},
        output_data={"prediction": int(result[0])},
        latency_ms=latency,
    )
    db.add(log)
    db.commit()

    return {"prediction": int(result[0]), "latency_ms": latency}
