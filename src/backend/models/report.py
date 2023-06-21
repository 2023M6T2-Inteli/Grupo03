from dotenv import load_dotenv
from pydantic import BaseModel

# Carrega variáveis do arquivo .env
load_dotenv()

class Relatorio(BaseModel):
    id: int
    nome_local: str
    endereco: str
    data: str
    gas: float
    observacoes: str