
from pydantic import BaseModel
from datetime import datetime

class StockPriceBase(BaseModel):
    datetime: datetime
    close: float
    
    high: float
    low: float
    open: float
    
    volume: int
    instrument: str

class StockPriceCreate(StockPriceBase):
    datetime: datetime
    close: float
    
    high: float
    low: float
    open: float
    
    volume: int
    instrument: str

class StockPriceResponse(StockPriceBase):
    id: int

    class Config:
        from_attributes = True
