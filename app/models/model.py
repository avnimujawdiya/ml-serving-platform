from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class MLModel(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    version = Column(String(20), nullable=False)
    framework = Column(String(50))
    file_path = Column(String(255), nullable=False)
    status = Column(String(20), default="active")
    created_at = Column(DateTime, server_default=func.now())
