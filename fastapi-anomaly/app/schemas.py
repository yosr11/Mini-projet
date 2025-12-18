from pydantic import BaseModel

class StockRequest(BaseModel):
    symbol: str
    from_date: str = "2018-01-01"
    to_date: str = "2025-12-01"
