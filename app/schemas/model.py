from pydantic import BaseModel
from datetime import datetime

class ModelCreate(BaseModel):
    name: str
    version: str
    framework: str
    file_path: str

class ModelResponse(BaseModel):
    id: int
    name: str
    version: str
    framework: str
    file_path: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
