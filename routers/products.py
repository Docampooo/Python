#importar APIrouter y HTTPException
from fastapi import APIRouter, HTTPException

#base model permite devolver json directamente tipando las variables
from pydantic import BaseModel

#declarar objeto tipo FastAPI()

#añadir tags para diferenciar datos y ordenar todo en la documentacion
router = APIRouter(prefix="/products", responses={404: {"message": "No encontrado"}})

lista_productos = ["P1", "P2", "P3", "P4"]

@router.get("/")
async def products():
    return lista_productos

@router.get("/products/{id}")
async def products(id: int):
    return lista_productos[id]