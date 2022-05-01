from fastapi import FastAPI
import uvicorn
from src.database import engine
from src.routers import client
import src.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SayolloAPI",
    description="REST API using FastApi & SqLite @ Aviv-biton",
    version="1.0",
)
app.include_router(client.router)

