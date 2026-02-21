from fastapi import APIRouter, HTTPException
from app.models.schemas import ExecuteRequest, ExecuteResponse
from app.core.broker_factory import get_broker
from app.core.execution_engine import ExecutionEngine
from app.notifications.notifier import NotificationService

router = APIRouter()


@router.post("/execute", response_model=ExecuteResponse)
def execute_portfolio(payload: ExecuteRequest):

    try:
        broker = get_broker(payload.broker)
        broker.authenticate(payload.credentials)

        engine = ExecutionEngine(broker)
        results = engine.execute_orders(payload.orders)

        notifier = NotificationService()
        notifier.notify(results)

        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))