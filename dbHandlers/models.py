from typing import Optional, Union

from pydantic import BaseModel, Field

from beanie import Document, Indexed, PydanticObjectId, Link

from bson import ObjectId

class UserDetails(BaseModel):
    id: str = Field(default="stri123123123ng", alias="_id")
    userName: str = "Fluff Robota"
    userImagePath: str = "some path"
    userRating: float = 4.99

class GameDetails(Document):
    gameName: Union[str, None] = None
    gameOwnerId: Union[str, None] = None
    gameDescriptionByClient: Union[str, None] = None
    gameDescription: Union[str, None] = None
    gamePlayerNo: Union[int, None] = None
    gameReccommandedAge: Union[int, None] = None
    gamePlayTime: Union[str, None] = None
    gameComplexity: Union[int, None] = None
    gameBGGRating: Union[int, None] = None # These will have added validation checks
    gameDesigners: Union[list, None] = None
    gameArtists: Union[list, None] = None
    gameMechanisms: Union[list, None] = None
    gameCategories: Union[list, None] = None
    class Settings:
        keep_nulls = False
        name = "Games"

class LinkTest(Document):
    testName: Union[str, None] = None
    testId: Union[str, None] = None
    testLink: Union[Link[GameDetails], str, None] = None

    class Settings:
        keep_nulls = False
        name = "ListingTests"

class GameObject(BaseModel):
    gameUserDetails: UserDetails
    gameDetails: GameDetails

class TestModel(BaseModel):
    test: UserDetails

    
