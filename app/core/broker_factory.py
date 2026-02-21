from app.brokers.zerodha import ZerodhaAdapter
from app.brokers.fyers import FyersAdapter
from app.brokers.angelone import AngelOneAdapter
from app.brokers.groww import GrowwAdapter
from app.brokers.upstox import UpstoxAdapter


def get_broker(name: str):

    brokers = {
        "zerodha": ZerodhaAdapter(),
        "fyers": FyersAdapter(),
        "angelone": AngelOneAdapter(),
        "groww": GrowwAdapter(),
        "upstox": UpstoxAdapter(),
    }

    if name.lower() not in brokers:
        raise Exception("Unsupported broker")

    return brokers[name.lower()]