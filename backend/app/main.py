from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine
from app.database.base import Base
from app.routers import auth_routes, resume_routes
from app.models import user, resume

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(resume_routes.router)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Resume Analyzer Running"}