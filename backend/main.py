from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import auth, employees, services, requests

app = FastAPI(
    title="GHS - Gestion des Heures Supplémentaires",
    description="API pour la gestion des heures supplémentaires",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routers
app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(services.router)
app.include_router(requests.router)

@app.get("/")
def root():
    return {"message": "GHS API - Gestion des Heures Supplémentaires"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
