import os
import fastapi
import asyncio
from supabase import Client
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from models import create_client, create_supabase_client
from fastapi.responses import FileResponse, StreamingResponse

app = FastAPI()

# URL e Chave de acesso 
url: str = "https://qeqhovaiuqfkrjywqayz.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlcWhvdmFpdXFma3JqeXdxYXl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTAxNjgwOSwiZXhwIjoyMDAwNTkyODA5fQ.0tuA_64ZpGS8olQikZBDzacoWr1Hj-srdCe46-5Mq90"  
models: Client = create_client(url, key)

#Nome do bucket utilizado - No meu caso é "Images"
bucket_name: str = "video"

@app.post("/upload-images")
async def upload_image(image: bytes = fastapi.File(...)): 
    with open("uploaded_image.jpg", "wb") as file:
        file.write(image)
    print(get_yolo_results("uploaded_image.jpg"))
    return {"message": "Image uploaded"}

@app.get('/video')
def video_feed(request:Request):
    return StreamingResponse(get_yolo_results(), media_type='multipart/x-mixed-replace; boundary=frame')

@app.get("/list")
async def list():
    res = models.storage.from_(bucket_name).list()
    print(res)

@app.post("/upload")
def upload(content: UploadFile = fastapi.File(...)):    
    with open(f"./recebidos/imagem{time.time()}.png", 'wb') as f:
        dados = content.file.read()
        f.write(dados)
    return {"status": "ok"}

list_files = os.listdir("./received")

@app.get("/images")
async def images():
    with open("./mock/lala.png", 'rb+') as f:
        arquivo = f.read()
        res = models.storage.from_(bucket_name).upload("lala.png", arquivo)
        print(res)
    return {"message": "Image uploaded successfully"}

models.Base.metadata.create_all(bind=engine)
