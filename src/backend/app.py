import httpx
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from models.report import Relatorio, create_supabase_client

app = FastAPI()


connected_clients = set()
schema_name = "public"  
table_name = "Relatorio"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/relatorios")
async def create_relatorio(relatorio: Relatorio):
    supabase = create_supabase_client()

    try:
        response = supabase.table(table_name).insert(relatorio.dict()).execute()
        print(response)
        return response
    except httpx.HTTPError as e:
        return {"message": "Erro ao criar o relatório: " + str(e)}

@app.get("/relatorios")
async def get_relatorios():
    supabase = create_supabase_client()
    
    response = supabase.table(table_name).select("*").execute()
    
    return response


@app.get("/relatorios/{id}")
async def get_relatorios(id: int):
    supabase = create_supabase_client()
     
    response = supabase.table(table_name).select("*").eq('id', str(id)).limit(1).execute()
    print(id)
    return response


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(data)
    except Exception as e:
        print(f"WebSocket connection closed with exception: {e}")
    finally:
        connected_clients.remove(websocket)