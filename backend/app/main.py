from fastapi import FastAPI
from app.api.v1.health import router as healt_router

app = FastAPI(
    title="StudyFlow API",
    description="Backend for StudyFlow app",
    version="0.1.0"
)

app.include_router(healt_router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "message": "StudyFlow API is running"
    }

