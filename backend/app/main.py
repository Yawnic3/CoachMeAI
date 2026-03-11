from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title = "CoachMe API",
    version = "0.1.0",
    description = "Backend API for CoachMe AI"
)

app.include_router(health_router)
app.include_router(analyze_router)

@app.get("/")

async def root():
    return {"message": "Welcome to the CoachMe API!"}