from dotenv import load_dotenv
from pydantic import BaseModel, Field
from itertools import count

load_dotenv()

class Relatorio(BaseModel):
    id: int = Field(default_factory=lambda: next(Relatorio._id_generator))
    nome_local: str
    endereco: str
    data: str
    observacoes: str
    gas: int
    _id_generator = count(1)