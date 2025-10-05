from database import SessionLocal
from fastapi import HTTPException
from datetime import datetime, date

def get_database():
    """Start and close database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
