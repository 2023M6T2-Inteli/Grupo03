from fastapi import APIRouter
from services.video_service import VideoService

router = APIRouter()

VIDEO_SERVICE = VideoService()

@router.post("/upload")
async def record():
    VIDEO_SERVICE.upload()
    return {"message": "Video salvo com sucesso!"}