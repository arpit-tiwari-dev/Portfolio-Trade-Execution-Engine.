from app.brokers.base import BrokerAdapter


class FyersAdapter(BrokerAdapter):

    def authenticate(self, credentials: dict) -> bool:
        return True

    def place_order(self, symbol: str, quantity: int, side: str) -> dict:
        return {
            "symbol": symbol,
            "quantity": quantity,
            "side": side,
            "status": "SUCCESS"
        }

    def get_holdings(self):
        return []