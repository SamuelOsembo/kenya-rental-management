from fastapi import FastAPI
from app.db.base import Base
from app.db.database import engine

app = FastAPI(
    title="Kenya Rental Management API",
    description="Backend API for a rental management SaaS platform.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Kenya Rental Management API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}

Base.metadata.create_all(bind=engine)