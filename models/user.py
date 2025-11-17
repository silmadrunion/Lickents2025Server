from typing import Optional, Union

from pydantic import BaseModel, Field

from beanie import Document, Indexed, PydanticObjectId, Link

from bson import ObjectId

class UserDetails(BaseModel):
    id: str = Field(default="stri123123123ng", alias="_id")
    userName: str = "Fluff Robota"
    userImagePath: str = "some path"
    userRating: float = 4.99

default_user = UserDetails()