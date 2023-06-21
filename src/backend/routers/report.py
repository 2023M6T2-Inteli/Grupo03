from fastapi import APIRouter
from models.report import Relatorio
from services.report_service import ReportService

router = APIRouter()

REPORT_SERVICE = ReportService()

@router.post("/relatorios")
async def create_relatorio(relatorio: Relatorio):
    try:
        response = REPORT_SERVICE.create(relatorio)
        return response
    except httpx.HTTPError as e:
        return {"message": "Erro ao criar o relatório: " + str(e)}

@router.get("/relatorios")
async def get_relatorios():
    response = REPORT_SERVICE.fetch()
    return response


@router.get("/relatorios/{id}")
async def get_relatorios(id: int):
    response = REPORT_SERVICE.fetch_by_id(id)
    return response