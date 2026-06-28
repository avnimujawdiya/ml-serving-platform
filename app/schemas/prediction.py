from pydantic import BaseModel
from typing import Any

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    prediction: Any
    latency_ms: float
