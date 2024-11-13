# schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RMABase(BaseModel):
    produto_id: int
    motivo: str
    status: Optional[str] = "pendente" 
class RMA(RMABase):
    id: int
    data_solicitacao: datetime

    class Config:
        from_attributes = True

class RMAUpdate(BaseModel):
    status: str 
