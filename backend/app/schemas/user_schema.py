from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Must include uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Must include lowercase letter")

        if not re.search(r"[^a-zA-Z0-9]", value):
            raise ValueError("Must include special character")

        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str