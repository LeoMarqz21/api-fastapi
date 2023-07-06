from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from jwt_manager import create_token
from middlewares.jwt_middleware import JWTBearer
from schemas.user import User

user_router = APIRouter()

@user_router.post('/auth/register', tags=['auth'])
def register(user: User):
    return JSONResponse(content=jsonable_encoder(user))

@user_router.post('/auth/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse({"token": token}, status_code=200)
    return JSONResponse({"error": "Invalid username or password"})

@user_router.post('/auth/logout', tags=['auth'])
def logout():
    pass

@user_router.post('/auth/refresh', tags=['auth'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def refresh():
    pass

@user_router.get('/auth/me', tags=['auth'], dependencies=[Depends(JWTBearer())])
def me():
    pass

@user_router.get('/auth/users', tags=['auth'], dependencies=[Depends(JWTBearer())])
def users():
    pass

@user_router.get('/auth/user/{id}', tags=['auth'], dependencies=[Depends(JWTBearer())])
def user(id: int):
    pass

@user_router.put('/auth/user/{id}', tags=['auth'], dependencies=[Depends(JWTBearer())])
def update_user(id: int):
    pass

@user_router.delete('/auth/user/{id}', tags=['auth'], dependencies=[Depends(JWTBearer())])
def delete_user(id: int):
    pass
