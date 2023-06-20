import os
from dotenv import load_dotenv
from pydantic import BaseModel
from supabase import create_client, Client

# Carrega variáveis do arquivo .env
load_dotenv()

# Acessa as variáveis do ambiente
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Relatorio(BaseModel):
    id: int
    nome_local: str
    endereco: str
    data: str
    gas: float
    observacoes: str


def create_supabase_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    return create_client(url, key)