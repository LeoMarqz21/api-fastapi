
#Schema
from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default='Mi pelicula', min_length=5, max_length=30) #validations
    overview: str = Field(default='Mi pelicula', min_length=5, max_length=100)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=25)

    class Config: #ejemplo de llenado de datos en swagger
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Avatar",
                "overview": "En un exuberante planeta llamado Pandora viven los navi.",
                "year": 2009,
                "rating": 7.8,
                "category": "Accion"
            }}