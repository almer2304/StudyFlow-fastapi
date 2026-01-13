from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

from app.api.v1.auth import router as auth_router

app = FastAPI(title="StudyFlow API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "StudyFlow API running"}

app.include_router(auth_router, prefix="/api/v1")

