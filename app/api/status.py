from fastapi import APIRouter
from typing import Literal
import random

router = APIRouter()

@router.get("/kandang")
def get_kandang_status() -> dict:
    amonia = random.uniform(0.2, 0.6)
    temperature = random.uniform(25, 35)

    status: Literal["CLEAR", "WARNING", "DANGEROUS"]
    if amonia > 0.5 or temperature > 34:
        status = "DANGEROUS"
    elif amonia > 0.35:
        status = "WARNING"
    else:
        status = "CLEAR"

    return {
        "status": status,
        "amonia": round(amonia, 2),
        "temperature": round(temperature, 2)
    }
