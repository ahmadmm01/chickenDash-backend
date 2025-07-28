from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import os

router = APIRouter()

# Function to simulate video processing
def stream_local_video():
    vid_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "videos", "cctv-video.mp4")
    with open(vid_path, "rb") as vid_file:
        yield from vid_file

@router.get("/result")
async def get_result_video():
    return StreamingResponse(stream_local_video(), media_type="video/mp4")