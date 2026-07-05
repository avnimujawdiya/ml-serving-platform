from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class RateLimit(Base):
    __tablename__ = "rate_limits"

    id = Column(Integer, primary_key=True)
    api_key = Column(String(64), nullable=False)
    window_start = Column(DateTime, nullable=False)
    request_count = Column(Integer, default=1)
    created_at = Column(DateTime, server_default=func.now())
