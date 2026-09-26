from sqlalchemy import false
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import RegisterRequest

router = APIRouter(prefix="/api/auth",tags =["auth"])

@router.post("/register")
def register(payload:RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()

    if existing:
        raise HTTPException(status_code=400,detail="Email already registered")
    new_user = User(email=payload.email, is_verified=False)
    db.add(new_user)
    db.commit()

    return{"message":"USer registered"}