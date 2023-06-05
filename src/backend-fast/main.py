from fastapi import FastAPI
from models import Relatorio, create_client, create_supabase_client
import httpx
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


schema_name = "public"  
table_name = "Relatorio"

#supafastgrupo3

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

