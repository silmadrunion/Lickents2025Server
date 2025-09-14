from fastapi import APIRouter, status

from typing import Union

from models.user import UserDetails, default_user
from models.game import GameDetails
from models.offer import OfferDetails, OfferObject

router = APIRouter(prefix="/offer")


# TO CHECK FROM HERE

@router.get("")
async def get_all_offers(user_id: Union[str, None] = None):
    if user_id:
        print("User Query Parameter provided: ", user_id)
    #gameObj = await handler.get_multiple_from_collection({"gameOwnerId": user_id}) #Recheck sometime
        offerObj = await OfferDetails.find({"offerOwnerId": user_id}).to_list()
    else:
        offerObj = await OfferDetails.find().to_list()
    print("DB RESULT:", offerObj)
    offerFinalResult = []
    for item in offerObj:
        gameList = []
        for gameId in item.offerGameIds:
            game = await GameDetails.get(gameId)
            gameList.append(game)
            print("Game: ", game)
        print("Game: ", gameList)
        item = OfferObject(offerDetails=default_user, offerDetails=item, offerGameDetails=gameList)
        print("Offer: ", item)
        offerFinalResult.append(item)
    print("Final ",offerFinalResult)
    return offerFinalResult

# TO CHECK FROM HERE

@router.get("/{listing_id}")
async def get_one_listing(listing_id):
    listing = await ListingDetails.get(listing_id)
    print(listing.listingGameId)
    game = await GameDetails.get(listing.listingGameId)
    listingObj = ListingObject(listingUserDetails=default_user, listingDetails=listing, listingGameDetails=game)
    return listingObj

# GET by offer? Probably not

@router.post("", status_code=status.HTTP_201_CREATED)
async def post_one_listing(listing: ListingDetails):
    print(listing.listingGameId)
    result = await listing.insert()    
    return listing

@router.put("", status_code=status.HTTP_201_CREATED)
async def put_one_listing(listing: ListingDetails):
    result = await listing.replace()
    return result

@router.patch("", status_code=status.HTTP_201_CREATED)
async def patch_one_listing(listing: ListingDetails):
   document_dict = {}
   for key, value in listing.model_dump().items():
       if value is not None:
           document_dict[key] = value
   result = await listing.update({'$set': document_dict})

@router.delete("/{listing_id}", status_code=status.HTTP_200_OK)
async def delete_one_listing(listing_id):
    listing = await ListingDetails.get(listing_id)
    print(listing)
    await listing.delete()
    return {}