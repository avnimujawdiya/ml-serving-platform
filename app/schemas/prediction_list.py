from pydantic import BaseModel
from typing import Any
from datetime import datetime

class PredictionOut(BaseModel):
    id: int
    model_id: int
    input_data: Any
    output_data: Any
    latency_ms: float | None
    created_at: datetime

    class Config:
        from_attributes = True
