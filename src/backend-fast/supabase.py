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

@app.get("/list")
async def list():
    # Lista todas as imagens do Bucket 
    res = models.storage.from_(bucket_name).list()
    print(res)

@app.get("/images")
# async def images(image: bytes = fastapi.File(...)):
async def images():
    # Rota da imagem local para ser feito o upload (no meu caso esta na pasta mock e é a imagem "lala.png")
    with open("./mock/lala.png", 'rb+') as f:
        arquivo = f.read()
        # Realiza o upload da imagem no bucket, sendo que o nome "lala.png" será o nome salvo no bucket, e você não pode criar imagens com o mesmo nome, emtão vale adicionar um timestamp pra garantir a diferença de nomes 

        res = models.storage.from_(bucket_name).upload("lala.png", arquivo)
        print(res)
    return {"message": "Image uploaded successfully"}