#importar APIRouter y HTTPException
from fastapi import APIRouter, HTTPException, status ,Depends

#modulo de autentificacion --> Gestion de contraseñas 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
import secrets
import os

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 60 # --> Una hora de sesion iniciada
SECRET = "mi_clave_secreta_super_segura_123"

#base model permite devolver json directamente tipando las variables
from pydantic import BaseModel

#declarar objeto tipo FastAPI()
router = APIRouter(prefix="/jwt_auth_users",responses={404: {"message": "No se ha encontrado el usuario"}})

#enviar la URL para autenticar
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["argon2"], deprecated="auto")

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
        "password": "$argon2i$v=19$m=16,t=2,p=1$Q0VTaTRLVVN3VGc2QVlJaA$SNlQrSGOjmLuo9DJ27Bgbw"
        },
    
    "benja": {
        "username": "Benja",
        "full_name": "Benja Crespo",
        "email": "benja@punk.com",
        "disable": True,
        "password": "$argon2i$v=19$m=16,t=2,p=1$Q0VTaTRLVVN3VGc2QVlJaA$tcQedJxspPRumRK8VJUgtg"
        },
    
    "adri": {
        "username": "adri",
        "full_name": "Adri Bastos",
        "email": "adri@swag.com",
        "disable": False,
        "password": "$argon2i$v=19$m=16,t=2,p=1$Q0VTaTRLVVN3VGc2QVlJaA$iT58Q13FwATvffLgurwpNQ"
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
    
    #una vez con el usuario
    user = search_userDB(form.username)
    
    #indica si se ha podido hashear la contraseña
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=404, detail="La contraseña no es correcta") 
        
    #tiempo que dura el token activo    
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    
    access_token = {"sub":user.username, "exp":expire}
    
    #Para no estar constantemente identificando al usuario se manda el token con el nombre de usuario
    return {"access_token": jwt.encode(access_token, SECRET ,algorithm = ALGORITHM), "token_type": "bearer"}

async def auth_user(token: str = Depends(oauth2)):
     
    excepcion = HTTPException(status_code= 401, detail="Error de autentificacion", headers={"WWW-Authenticate-error": "Bearer"})
    
    try:
        
        #obtener los datos del usuario
        username = jwt.decode(token, SECRET ,algorithms=[ALGORITHM]).get("sub")
        
        if username is None:
            raise excepcion
        
        user = search_user(username)
        return user
            
    except:
        raise excepcion 
        
#capturar el token creado en el login para mantener la sesion iniciada
async def current_user(user: User = Depends(auth_user)):

    if user.disable:
        raise HTTPException(status_code= 400, detail="El usuario está inactivo", headers={"WWW-Authenticate-error": "Bearer"}) 
        
    #devolver usuario
    return user

#funcion para obtener el usuario ya loggeado
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user