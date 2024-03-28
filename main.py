from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from confing.database import  engine, Base
from middlewares.error_handler import Erro_Handler
from routers.movie import movie_router
from routers.users import user_router
import socket
  
app = FastAPI()
app.title = 'python me salvara'
app.version = '0.0.1'

app.add_middleware(Erro_Handler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind = engine)


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "IronMan",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2007",
        "rating": 7.8,
        "category": "Acción"
    },
]

@app.get('/', tags=['home'])
def messages():
    return HTMLResponse('<h1>sere el mejor</h1>')



def obtener_ip():
    nombre_host = socket.gethostname()
    print(nombre_host)
    ip_local = socket.gethostbyname(nombre_host)
    return ip_local


if __name__ == '__main__':
    ip = obtener_ip()
    print(ip)

