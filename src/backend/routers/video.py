from fastapi import APIRouter
from services.video_service import VideoService

router = APIRouter()

VIDEO_SERVICE = VideoService()

@router.post("/upload")
async def upload(id):
    VIDEO_SERVICE.upload(id)
    return {"message": "Video salvo com sucesso!"}

@router.get("/get-video-url")
async def get_video_url(id):
    url = VIDEO_SERVICE.fetch_by_id(id)
    return {"message": "URL do vídeo obtida com sucesso!", "url": url}