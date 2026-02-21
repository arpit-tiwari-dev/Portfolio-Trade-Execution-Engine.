from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Portfolio Trade Execution Engine")

app.include_router(router)