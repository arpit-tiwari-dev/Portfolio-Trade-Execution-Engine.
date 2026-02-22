# 📘 Portfolio Trade Execution Engine

---

## 🚀 Overview

This project implements an end-to-end **Portfolio Trade Execution Engine** using **FastAPI**, designed to bridge systematic portfolio models with broker execution infrastructure.

The system:

* Accepts a desired portfolio state
* Authenticates with a selected broker
* Places  trades
* Returns execution summary via notification system
* Is fully containerized using Docker

The architecture is modular, broker-agnostic, and built with production-style separation of concerns.

---

## 🏗 Architecture Overview

```
API Layer (FastAPI)
        ↓
Execution Engine (Core Domain Logic)
        ↓
Broker Adapter Layer (Strategy Pattern)
        ↓
Notification Layer
```

### Core Design Principles

* Adapter Pattern for broker integration
* Clear separation between domain logic and API layer
* Idempotent execution design
* Retry handling for transient failures
* Strong typing via Pydantic domain models
* Extensible broker factory architecture

---

## 📂 Project Structure

```
app/
 ├── api/                # FastAPI routes
 ├── brokers/            # Broker adapters (Adapter Pattern)
 ├── core/               # Execution engine & broker factory
 ├── domain/             # Domain models (OrderResult, OrderStatus)
 ├── models/             # API request/response schemas
 ├── notifications/      # Notification system
 └── main.py
```

## 🔌 Broker Integration (Adapter Pattern)

Each broker implements a standardized interface:

```python
class BrokerAdapter(ABC):
    def authenticate(self, credentials: dict) -> bool
    def place_order(self, symbol: str, quantity: int, side: str)
    def get_holdings(self) -> list
```

### Why Adapter Pattern?

* Decouples execution engine from broker SDK specifics
* Adding a new broker requires only:

  * Implementing `BrokerAdapter`
  * Registering it in `broker_factory.py`
* No changes required in execution engine

---

## 🏦 Supported Brokers (Mocked for Assignment Safety)

* Zerodha
* Fyers
* AngelOne
* Groww
* Upstox

For security and reproducibility, broker APIs are mocked while preserving realistic behavior:

* Stateful holdings
* Order execution updates holdings
* Random API failure simulation
* Retry logic

---

## 📣 Notification System

After execution completes:

* Execution summary is logged
* Failed orders are clearly reported
* Structure supports WebSocket/Webhook extension

---

## 🧪 Example Request

```json
POST /execute
{
  "broker": "zerodha",
  "credentials": {
    "api_key": "demo",
    "access_token": "demo"
  },
  "target_portfolio": [
    {"symbol": "RELIANCE", "target_quantity": 20},
    {"symbol": "TCS", "target_quantity": 0}
  ]
}
```

---

## 📊 Example Response

```json
{
  "results": [
    {
      "symbol": "RELIANCE",
      "quantity": 10,
      "side": "BUY",
      "status": "FILLED",
      "reason": null
    },
    {
      "symbol": "TCS",
      "quantity": 5,
      "side": "SELL",
      "status": "FILLED",
      "reason": null
    }
  ]
}
```

---

## 🐳 Running with Docker

### 1️⃣ Build & Run

```bash
docker-compose up --build
```

### 2️⃣ Access API Docs

```
http://localhost:8000/docs
```

Swagger UI allows interactive testing.

---

## ⚙️ Architectural Decisions

### 1. Domain Models Separate from API Models

Execution layer uses `OrderResult` domain model to avoid tight coupling with API schemas.

---

### 2. Broker Factory Pattern

Broker instances are managed centrally via factory to:

* Maintain stateful holdings
* Simulate real brokerage behavior
* Avoid re-instantiation on every request

---

### 3. No Database (Intentional)

Since assignment scope focuses on execution engine, in-memory state simulation was chosen to:

* Keep scope focused
* Demonstrate delta logic clearly
* Maintain reproducibility

---

### 4. Mocked Broker Layer

Real broker SDKs require OAuth, live keys, and environment configuration.

For assignment safety:

* Broker behavior is simulated
* Execution logic remains realistic
* Interface design remains production-ready

---

## 🔮 How to Add a 6th Broker

1. Create new adapter in `app/brokers/`
2. Implement `BrokerAdapter`
3. Register broker in `broker_factory.py`

No other code changes required.

---

## 📈 Possible Enhancements

* Async order execution
* WebSocket notifications
* Real broker SDK integration
* Risk management layer
* Persistent order tracking
* Execution audit logs
* Slippage simulation
* Partial fill modeling

---

## 🎯 Conclusion

This implementation focuses on:

* Clean infrastructure design
* Broker abstraction
* Robust execution handling
* Production-style modularity

The system is built to reflect how systematic quantitative strategies interface with brokerage execution systems in a real-world environment.
