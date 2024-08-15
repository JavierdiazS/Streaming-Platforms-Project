#Modularizar o dividir nuestros routers
from fastapi import APIRouter
from config.db import engine
from models.user import streaming, actors, gender
from sqlalchemy import func, select

user = APIRouter()

# 1. Number of movies and series (separate) per platform
@user.get("/get_count_platform/{platform}", tags=["Querys"])
def get_count_platform(platform:str):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(streaming.c.category).label("Amount"),streaming.c.category)                            
                            .where(streaming.c.platform==platform)
                            .group_by(streaming.c.category)
                            )
        
        return result.fetchall()

# 2. Maximum duration according to type of film (film/series), by platform and by year
@user.get("/get_max_duration/{year}/{platform}/{tipo}", tags=["Querys"])
def get_max_duration(year:int,platform:str,tipo:str):
    with engine.connect() as conn:
        result = conn.execute(select(streaming.c.duration,streaming.c.title)
                            .where(streaming.c.release_year==year)
                            .where(streaming.c.platform==platform)
                            .where(streaming.c.type_duration==tipo)
                            .order_by(streaming.c.duration.desc())
                            )
        
        return result.first()

# 3. Actor with the most repetitions according to platform and year
@user.get("/get_actor/{platform}", tags=["Querys"])
def get_actor(platform:str,year:int):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(cast_table.c.cast).label("appearances_quantity"),cast_table.c.cast)
                                    .join(streaming,streaming.c.idStream==cast_table.c.idStream)
                                    .where(streaming.c.release_year == year)
                                    .where(streaming.c.platform==platform)
                                    .where(cast_table.c.cast!="no data")
                                    .group_by(cast_table.c.cast)
                                    .order_by(func.count(cast_table.c.cast).desc()))
       
        return result.first()

#4. Number of times a genre and platform are repeated most frequently
@user.get("/get_listedin/{genre}", tags=["Querys"])
def get_listedin(genre:str):
    with engine.connect() as conn:
        result = conn.execute(select(streaming.c.platform,func.count(streaming.c.platform).label("repeated_quantity"))
                            .join(genre_table,streaming.c.idStream==genre_table.c.idStream)
                            .where(genre_table.c.genre == genre)
                            .group_by(streaming.c.platform)
                            .order_by(func.count(streaming.c.platform).desc()) )
        
        return result.first()