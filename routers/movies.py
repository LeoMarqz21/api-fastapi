from fastapi import APIRouter, Depends,Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_middleware import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()

@movie_router.get("/movies", tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies()->List[Movie]:
    movies = MovieService(db=Session()).get_movies()
    movies = jsonable_encoder(movies)
    return JSONResponse(content=movies, status_code=200)

#get normal
@movie_router.get("/movies/{id}", tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000))->Movie: #ge: >= 1, le: <= 2000, Path es validador de parametros de ruta
    movie = MovieService(db=Session()).get_movie(id=id)
    if movie is not None:
            return JSONResponse(content=jsonable_encoder(movie), status_code=200)
    return JSONResponse(content={"message": f"Movie [{id}] not found"}, status_code=404)

#/movie/ representa un query string
@movie_router.get('/movies/', tags=['movies'])
def get_movie_by_category(category: str = Query(min_length=3, max_length=15)): #Query valida parametros de query string
    movies = jsonable_encoder(
        MovieService(db=Session())
            .get_movies_by_category(category)
        )
    return JSONResponse(content=movies, status_code=200)

# def create_movie(id:int = Body(), title:str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category:str = Body()):
@movie_router.post("/movies", tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie)->dict:
    MovieService(db=Session()).create_movie(movie)
    return JSONResponse(content={"message": "Movie created", "status": "success"}, status_code=201)

@movie_router.put("/movies/{id}", tags=['movies'], response_model=dict, status_code=200)
def update_movie(id:int, movie:Movie)->dict:
    result = MovieService(db=Session()).update_movie(id, movie)
    if not result:
        return JSONResponse(content={"message": f"Movie [{id}] not found", "status": "error"}, status_code=404)
    return JSONResponse(content={"message": f"Movie [{id}] updated", "status": "success"}, status_code=200)

@movie_router.delete("/movies/{id}", tags=['movies'])
def delete_movie(id:int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found", "status": "error"}, status_code=404)
    db.delete(result)
    db.commit()
    return JSONResponse(content={"message": f"Movie [{id}] deleted", "status": "success"}, status_code=200)


