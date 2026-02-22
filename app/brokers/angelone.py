from app.brokers.base import BrokerAdapter
from app.models.schemas import OrderResult


class AngelOneAdapter(BrokerAdapter):

    def authenticate(self, credentials: dict) -> bool:
        return True

    def place_order(self, symbol: str, quantity: int, side: str) -> dict:
        return OrderResult(
            symbol=symbol,
            quantity=quantity,
            side=side,
            status="Success",
        )

    def get_holdings(self):
        return []