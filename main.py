#importar fastAPI y HTTPException
from fastapi import FastAPI, HTTPException

#base model permite devolver json directamente tipando las variables
from pydantic import BaseModel

#declarar objeto tipo FastAPI()
app = FastAPI()

#Routers
from routers import users, products, basis_auth_users, jwt_auth_users

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basis_auth_users.router)
app.include_router(jwt_auth_users.router)

#recursos estáticos
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

#para hacer el equivalente a un package --> uvicorn main:app --reload
#ruta http://127.0.0.1:8000/

#getters
@app.get("/saludo")
async def root():
    return { "saludo" : "mi nombre es Nico!"}