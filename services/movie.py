from typing import List
from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService:
    def __init__(self, db):
        self.db = db
    
    def get_movies(self)->List[Movie]:
        return self.db.query(MovieModel).all()
    
    def get_movie(self, id: int)->Movie:
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_movies_by_category(self, category:str)->List[Movie]:
        return self.db.query(MovieModel).filter(MovieModel.category == category).first()
    
    def create_movie(self, movie: Movie)->None:
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 

    def update_movie(self, id:int, data: Movie)->Movie:
        movie:MovieModel = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not movie:
            return None
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return movie
    
    def delete_movie(self, id:int)->Movie:
        pass