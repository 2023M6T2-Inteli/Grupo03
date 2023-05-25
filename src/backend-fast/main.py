from fastapi import FastAPI
from models import Relatorio, create_client, create_supabase_client
import httpx

app = FastAPI()


schema_name = "public"  # Substitua pelo nome do esquema correto
table_name = "Relatorio"

#supafastgrupo3

@app.post("/relatorios")
async def create_relatorio(relatorio: Relatorio):
    supabase = create_supabase_client()
    
    try:
    # Crie uma nova entrada no Supabase
        response = supabase.table(table_name).insert(relatorio.dict()).execute()
        print(response)
    # Verifique se a inserção foi bem-sucedida
        return response
    except httpx.HTTPError as e:
        return {"message": "Erro ao criar o relatório: " + str(e)}

@app.get("/relatorios")
async def get_relatorios():
    supabase = create_supabase_client()
    
    # Faça uma consulta para obter todos os relatórios
    response = supabase.table(table_name).select("*").execute()
    
    return response


@app.get("/relatorios/{id}")
async def get_relatorios(id: int):
    supabase = create_supabase_client()
     
    # Faça uma consulta para obter todos os relatórios
    response = supabase.table(table_name).select("*").eq('id', str(id)).limit(1).execute()
    print(id)
    return response
