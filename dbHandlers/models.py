from typing import Optional

import pymongo
from pydantic import BaseModel

from beanie import Document, Indexed

class UserDetails(BaseModel):
    id: str = "stri123123123ng"
    userName: str = "Fluff Robota"
    userImagePath: str = "some path"
    userRating: float = 4.99

class GameDetails(Document):
    gameName: str
    gameDescriptionByClient: str = ""
    gameDescription: str =""
    gamePlayerNo: int
    gameReccommandedAge: Optional[int]
    gamePlayTime: str = ""
    gameComplexity: Optional[int]
    gameBGGRating: Optional[int] # These will have added validation checks
    gameDesigners: list[str] = []
    gameArtists: list[str] = []
    gameMechanisms: list[str] = []
    gameCategories: list[str] = []

class GameObject(BaseModel):
    gameUserDetails: UserDetails
    gameDetails: GameDetails


    
