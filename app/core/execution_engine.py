import time
from app.models.schemas import OrderResult


class ExecutionEngine:

    def __init__(self, broker):
        self.broker = broker

    def execute_orders(self, orders):
        results = []

        for order in orders:

            for attempt in range(3):
                try:
                    response = self.broker.place_order(
                        symbol=order.symbol,
                        quantity=order.quantity,
                        side=order.action
                    )

                    results.append(response)
                    break

                except Exception as e:

                    if attempt == 2:
                        results.append(OrderResult(
                            symbol=order.symbol,
                            quantity=order.quantity,
                            side=order.action,
                            status="FAILED",
                            reason=str(e)
                        ))
                    else:
                        time.sleep(1)

        return results