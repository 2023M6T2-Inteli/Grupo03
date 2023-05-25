from dotenv import load_dotenv
import os
from typing import List
from pydantic import BaseModel
from supabase import create_client, Client

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis do ambiente
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Relatorio(BaseModel):
    id: int
    nome_local: str
    endereco: str
    data: str
    gas: float
    condicoes_ambientais: str
    observacoes: str


def create_supabase_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    return create_client(url, key)