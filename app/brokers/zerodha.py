import random
from app.brokers.base import BrokerAdapter
from app.models.schemas import OrderResult


class ZerodhaAdapter(BrokerAdapter):

    def authenticate(self, credentials: dict) -> bool:
        return True

    def place_order(self, symbol: str, quantity: int, side: str) -> OrderResult:
        # Simulate occasional failure
        if random.random() < 0.1:
            raise Exception("Zerodha API rate limit exceeded")

        return OrderResult(
            symbol=symbol,
            quantity=quantity,
            side=side,
            status="Success",
        )

    def get_holdings(self):
        return []