from abc import ABC, abstractmethod


class BrokerAdapter(ABC):

    @abstractmethod
    def authenticate(self, credentials: dict) -> bool:
        pass

    @abstractmethod
    def place_order(self, symbol: str, quantity: int, side: str) -> dict:
        pass

    @abstractmethod
    def get_holdings(self) -> list:
        pass