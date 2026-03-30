from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.user import User
from app.utils.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    print("\n--- AUTH DEBUG START ---")

    if not credentials:
        print("❌ No credentials received")
        raise HTTPException(status_code=401, detail="No credentials")

    token = credentials.credentials
    print("✅ TOKEN RECEIVED:", token)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("✅ DECODED PAYLOAD:", payload)

        user_id = payload.get("user_id")
        print("✅ USER ID:", user_id)

    except Exception as e:
        print("❌ JWT ERROR:", str(e))
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == user_id).first()
    print("✅ USER FOUND:", user)

    print("--- AUTH DEBUG END ---\n")

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user