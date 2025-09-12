from typing import Optional, Union

from pydantic import BaseModel, Field

from beanie import Document, Indexed, PydanticObjectId, Link

from bson import ObjectId

from models.user import UserDetails
from models.game import GameDetails


class ListingDetails(Document):
    listingOwnerId: Union[str, None] = None
    listingGameId: Union[str, None] = None
    listingOfferIds: Union[list, None] = None
    class Settings:
        keep_nulls = False
        name = "ListingTests"

class ListingObject(BaseModel):
    listingUserDetails: UserDetails
    listingDetails: ListingDetails
    listingGameDetails: GameDetails