from fastapi import FastAPI
from api import video, sensor, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Smart Chicken Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video.router, prefix="/video")
app.include_router(sensor.router, prefix="/sensor")
app.include_router(status.router, prefix="/status")
