from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SENTINEL-X API",
    version="0.1.0",
    description="Defensive cyber intelligence and threat analysis API.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "operational", "service": "sentinel-x-api", "version": "0.1.0"}

@app.get("/api/v1/system/status")
def system_status() -> dict:
    return {
        "platform": "SENTINEL-X",
        "environment": "development",
        "mode": "defensive-research",
        "data_mode": "synthetic",
        "services": {
            "api": "operational",
            "intelligence": "standby",
            "correlation": "standby",
            "ai": "standby",
        },
    }
