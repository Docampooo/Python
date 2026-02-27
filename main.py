#importar fastAPI
from fastapi import FastAPI

#base model permite devolver json directamente tipando las variables
from pydantic import BaseModel

#declarar objeto tipo FastAPI()
app = FastAPI()

#para hacer el equivalente a un package --> uvicorn main:app --reload

#getters
@app.get("/saludo")
async def root():
    return { "saludo" : "mi nombre es Nico!"}

#clase Usuario
class User(BaseModel):
    
    id: int
    name: str
    surname: str
    age: int

#base de datos local de usuarios
users = [User(id = 1, name ="Nico", surname = "Docampo", age = 20), 
         User(id = 2, name = "Diego", surname = "Pinheiro", age = 21), 
         User(id = 3, name = "Alberto", surname = "Carril", age = 25)]

#devolver json
@app.get("/usersjson")
async def usersjson():
    return users

def search_user(id: int):
    try:
        #Devuelve el usuario con dicho id
        res = filter(lambda user: user.id == id, users)
            
        return list(res)[0]
        
    except:
        return {"error":"No se ha encontrado el usuario"}

#PathParam en el get
@app.get("/user/{id}")
async def user(id: int):
    
    return search_user(id)
    
#query params --> tipado de variables
@app.get("/userquery/")
async def userquery(id: int):
    
    return search_user(id)

#Post
@app.post("/user/")
async def user(user: User):
    
    if type(search_user(user.id)) == User:
        
        return {"error":"El usuario ya existe"}
    else:
        
        users.append(user)
        return user
    
#Put
#reemplazar un usuario por otro
@app.put("/user/{id}")
async def user(user: User, id: int):
    
    found = False
    for index, u in enumerate(users):
        if u.id == id:
            users[index] = user
            found = True
    
    if not found:
        return {"error":"El usuario no se ha encontrado"}
    
    return user

#Delete
@app.delete("/user/{id}")
async def user(id: int):
    
    user = None
    found = False
    for index, u in enumerate(users):
        
        if u.id == id:
            del users[index]
            user = u
            found = True
            
    if not found:
        return {"error":"El usuario no se ha encontrado"}
    
    return user