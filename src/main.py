from fastapi import FastAPI
from src.models import models
from fastapi.middleware.cors import CORSMiddleware
from src.router import router as api_router
from src.database.database import engine, Base

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(api_router)
