from fastapi import HTTPException, Depends, Header, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.db.session import get_db
from app.models.rate_limit import RateLimit

RATE_LIMIT = 5
WINDOW_MINUTES = 1

def check_rate_limit(
    x_api_key: str = Header(..., alias="X-API-Key"),
    db: Session = Depends(get_db),
):
    now = datetime.utcnow()
    window_start = now - timedelta(minutes=WINDOW_MINUTES)

    count = db.query(func.sum(RateLimit.request_count))\
        .filter(
            RateLimit.api_key == x_api_key,
            RateLimit.window_start >= window_start,
        ).scalar() or 0

    if count >= RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Max {RATE_LIMIT} requests per {WINDOW_MINUTES} minute.",
        )

    log = RateLimit(api_key=x_api_key, window_start=now)
    db.add(log)
    db.commit()
