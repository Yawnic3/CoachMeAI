from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes.health import router as health_router
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    description = "Backend API for CoachMe AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(analyze_router)

@app.get("/")

async def root():
    return {"message": "Welcome to the CoachMe API!"}