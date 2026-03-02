#importar APIRouter y HTTPException
from fastapi import APIRouter, HTTPException, status ,Depends

#modulo de autentificacion --> Gestion de contraseñas 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#base model permite devolver json directamente tipando las variables
from pydantic import BaseModel

#declarar objeto tipo FastAPI()
router = APIRouter(prefix="/basis_auth_users",responses={404: {"message": "No se ha encontrado el usuario"}})

#enviar la URL para autenticar
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

#clase Usuario con el que se trabaja
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool
    
#Usuario que se envia a la base de datos
class UserDB(User):
    password: str

#base de datos con los usuarios
users_db = {
    "nico": {
        "username": "nico",
        "full_name": "Nico Docampo",
        "email": "nico@metal.com",
        "disable": False,
        "password": "1234"
        },
    
    "benja": {
        "username": "Benja",
        "full_name": "Benja Crespo",
        "email": "benja@punk.com",
        "disable": True,
        "password": "punk"
        },
    
    "adri": {
        "username": "adri",
        "full_name": "Adri Bastos",
        "email": "adri@swag.com",
        "disable": False,
        "password": "4321"
        }
}

@router.get("/")
async def hola():
    return "hola"

#buscar usuario por nombre
def search_user(username: str):
    
    if(username in users_db):
        return User(**users_db[username])
    
def search_userDB(username: str):
    
    if(username in users_db):
        return UserDB(**users_db[username])

#funcion para iniciar sesion
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    #buscar usuario en la base de datos
    user_db = users_db.get(form.username)
    
    if not user_db:
        raise HTTPException(status_code=404, detail="El usuario no es correcto") 
    
    user = search_userDB(form.username)
    
    if not form.password == user.password:
        raise HTTPException(status_code=404, detail="La contraseña no es correcta") 
        
    #Para no estar constantemente identificando al usuario se manda el token con el nombre de usuario
    return {"access_token": user.username, "token_type": "bearer"}

#capturar el token creado en el login para mantener la sesion iniciada
async def current_user(token: str = Depends(oauth2)):
    
    user = search_user(token)
    if not user:
        raise HTTPException(status_code= 401, detail="Error de autentificacion", headers={"WWW-Authenticate-error": "Bearer"}) 

    if user.disable:
        raise HTTPException(status_code= 400, detail="El usuario está inactivo", headers={"WWW-Authenticate-error": "Bearer"}) 
        
    #devolver usuario
    return user

#funcion para obtener el usuario ya loggeado
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user