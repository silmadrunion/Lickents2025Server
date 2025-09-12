from typing import Optional, Union

from pydantic import BaseModel, Field

from beanie import Document, Indexed, PydanticObjectId, Link

from bson import ObjectId

from models.user import UserDetails
from models.game import GameDetails


class OfferDetails(Document):
    offerOwnerId: Union[str, None] = None
    offerGameIds: Union[list, None] = None
    listingOfferIds: Union[list, None] = None
    class Settings:
        keep_nulls = False
        name = "OfferTests"

class OfferObject(BaseModel):
    offerUserDetails: UserDetails
    offerDetails: OfferDetails
    offerGameDetails: list[GameDetails]