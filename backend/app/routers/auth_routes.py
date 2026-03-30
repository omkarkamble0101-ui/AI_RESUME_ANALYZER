from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.utils.auth import hash_password, verify_password
from app.utils.security import create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hased = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hased
    )
    db.add(new_user)
    db.commit()
    
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user or not verify_password(user.password, db_user.password):
        return {"message": "Invalid credentials"}
    
    access_token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }