import random
from app.brokers.base import BrokerAdapter


class ZerodhaAdapter(BrokerAdapter):

    def authenticate(self, credentials: dict) -> bool:
        return True

    def place_order(self, symbol: str, quantity: int, side: str) -> dict:
        # Simulate occasional failure
        if random.random() < 0.1:
            raise Exception("Zerodha API rate limit exceeded")

        return {
            "symbol": symbol,
            "quantity": quantity,
            "side": side,
            "status": "SUCCESS"
        }

    def get_holdings(self):
        return []