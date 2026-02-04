from pydantic import BaseModel
from datetime import datetime

class ProgramacaoEntrega(BaseModel):
    material: str
    volume: float
    data_horario_previsto: datetime
