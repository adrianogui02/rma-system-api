# schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RMABase(BaseModel):
    produto_id: str
    motivo: str
    status: Optional[str] = "pendente" 
class RMA(RMABase):
    id: str
    data_solicitacao: datetime

    class Config:
        from_attributes = True

class RMAUpdate(BaseModel):
    status: str 
