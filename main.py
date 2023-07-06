from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from config.database import Base, Engine
from middlewares.error_handler import ErrorHandler
from routers.movies import movie_router
from routers.users import user_router

app = FastAPI()
#Titulo en /docs => swagger
app.title = 'Mi aplicacion con FastApi'
app.version = '0.0.1'

#middlewares
app.add_middleware(ErrorHandler)

#routers
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=Engine)

@app.get("/", tags=['home'])
def home():
    return HTMLResponse('<h1>Hello World</h1')

