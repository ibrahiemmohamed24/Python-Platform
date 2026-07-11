from fastapi import FastAPI

from app.routers.health import router as health_router

app = FastAPI(
    title="AI Python QA Platform",
    description="AI-powered Python Quality Assurance Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Python QA Platform 🚀"
    }


app.include_router(health_router)