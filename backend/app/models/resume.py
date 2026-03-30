from sqlalchemy import Column, Integer, Text, String, ForeignKey, TIMESTAMP
from datetime import datetime
from app.database.base import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    file_name = Column(String)
    extracted_text = Column(Text)
    score = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
