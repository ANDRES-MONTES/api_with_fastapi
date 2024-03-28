from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from confing.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from serivces.movie import MovieServices
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model = List[Movie], status_code = 200, dependencies=[Depends(JWTBearer())])
def get_movies():
    db = Session()
    result = MovieServices(db).get_movies()
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model = List[Movie])
def get_movie(id:int = Path(ge = 1, le=2000)):
    db =Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code = 404, content={'message': 'no encontrado'})
        
    return JSONResponse(status_code = 200, content=jsonable_encoder(result))
    #result = list(filter(lambda x : x['id'] == id, movies))
    #if len(result) > 0:
     #   return JSONResponse(content = result)
    #else:
        #return JSONResponse(status_code = 404, content = result)
        

@movie_router.get('/movies/', tags=['movies'], response_model = List[Movie])
def get_movies_by_category(category:str = Query(min_length = 5, max_length = 20)):
    db = Session()
    result = MovieServices(db).get_movie_category(category)
    if not result:
        return JSONResponse(status_code = 404, content = {'message':'no encontrado'})
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))
    # result = list(filter(lambda x : x['category'] == category, movies))
    # return JSONResponse(content = result)
    
@movie_router.post('/movies', tags=['movies'], response_model = dict, status_code = 201)
def create_movie(movie:Movie):
    db = Session()
    MovieServices(db).create_movie(movie)
    #movies.append(movie)
    return JSONResponse(status_code = 201, content={'message': 'se ha registrado la pelicula'})

@movie_router.put('/movies/{id}', tags=['movies'],  response_model = dict)
def update_movie(id:int, movie: Movie):
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message':'no encontrado'})
    
    # for i in movies:
    #     if i['id'] == id:
    #         movie.id = id
    #         i.update(movie)
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(content={'message': 'se ha modificado la pelicula'})
        
@movie_router.delete('/movies/{id}', tags=['movies'],  response_model = dict)
def delete_movie(id:int):
    db = Session()
    result:MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message':'no encontrado'})
    # for i in range(len(movies)):
    #     if movies[i]['id'] == id:
    #         del movies[i]
    #         break
    MovieServices(db).delete_movie(id)
    return JSONResponse(content={'message': 'se ha eliminado la pelicula'})
        
                         
        