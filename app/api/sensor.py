from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

@router.get("/realtime")
def get_sensor_data():
    return {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(60, 90), 2),
        "amonia": round(random.uniform(0.2, 0.6), 2),
        "co2": round(random.uniform(400, 1000), 2),
        "light": round(random.uniform(200, 800), 2),
        "timestamp": datetime.now().isoformat() + "Z"
    }
