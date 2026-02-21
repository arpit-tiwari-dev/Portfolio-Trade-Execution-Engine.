from pydantic import BaseModel
from typing import List, Dict


class Order(BaseModel):
    symbol: str
    quantity: int
    action: str  # BUY / SELL


class ExecuteRequest(BaseModel):
    broker: str
    credentials: Dict[str, str]
    orders: List[Order]


class OrderResult(BaseModel):
    symbol: str
    quantity: int
    side: str
    status: str
    reason: str | None = None


class ExecuteResponse(BaseModel):
    results: List[OrderResult]