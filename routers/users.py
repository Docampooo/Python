#importar APIRouter y HTTPException
from fastapi import APIRouter, HTTPException

#base model permite devolver json directamente tipando las variables
from pydantic import BaseModel

#declarar objeto tipo FastAPI()
router = APIRouter(prefix="/users",responses={404: {"message": "No se ha encontrado el usuario"}})

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
@router.get("/usersjson")
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
@router.get("/user/{id}")
async def user(id: int):
    
    return search_user(id)
    
#query params --> tipado de variables
@router.get("/userquery/")
async def userquery(id: int):
    
    return search_user(id)

#Post --> añade un usuario a la lista, indica lo que devuelve y indica el Response en la cabecera
@router.post("/user/", response_model= User ,status_code=201)
async def user(user: User):
    
    if type(search_user(user.id)) == User:
        
        #lanzar excepcion con la respuesta en caso de que la consulta no sea existosa
        raise HTTPException(status_code=304 , detail="El usuario ya existe")
        
    else:
        
        users.append(user)
        return user
    
#Put
#reemplazar un usuario por otro
@router.put("/user/{id}", status_code=200)
async def user(user: User, id: int):
    
    found = False
    for index, u in enumerate(users):
        if u.id == id:
            users[index] = user
            found = True
    
    if not found:
        
        raise HTTPException(status_code=404, detail="El usuario no se ha encontrado")
    return user

#Delete
@router.delete("/user/{id}", response_model= User, status_code=200)
async def user(id: int):
    
    user = None
    found = False
    for index, u in enumerate(users):
        
        if u.id == id:
            del users[index]
            user = u
            found = True
            
    if not found:
        return HTTPException(status_code=404, detail="No se ha encontrado el usuaio")
    
    return user