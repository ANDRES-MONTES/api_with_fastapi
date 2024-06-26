from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id : Optional[int] | None
    title : str = Field(min_length = 5, max_length= 15)
    overview : str = Field(min_length =15, max_length= 50)
    year : int = Field(le=2022)
    rating: float = Field(ge=0, lt=100)
    category : str = Field(min_length =5, max_length= 20)
    
        
    class Config:
        json_schema_extra = {
            'example': {
                'id' : 1,
                'title' : 'mi pelicula',
                'overview' : 'Descripccion de pelicula',
                'year' : 2022,
                'rating' : 7.0,
                'category' : 'Acción'
            }
        }
