from fastapi import APIRouter, status

from typing import Union

from models.user import UserDetails, default_user
from models.listing import ListingDetails
from models.game import GameDetails
from models.offer import OfferDetails, OfferObject

router = APIRouter(prefix="/offer")

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
        item = OfferObject(offerUserDetails=default_user, offerDetails=item, offerGameDetails=gameList)
        print("Offer: ", item)
        offerFinalResult.append(item)
    print("Final ",offerFinalResult)
    return offerFinalResult

@router.get("/{offer_id}")
async def get_one_listing(offer_id):
    offer = await OfferDetails.get(offer_id)
    print(offer.offerGameIds)
    gameList = []
    for gameId in offer.offerGameIds:
            game = await GameDetails.get(gameId)
            gameList.append(game)
            print("Game: ", game)
    offerObj = OfferObject(offerUserDetails=default_user, offerDetails=offer, offerGameDetails=gameList)
    return offerObj

#Add updating Listing on creating Offer ; Mongo $push for the .update() function
#Rerouting/Batching in case of fails ; Write Concern Errors ; 

@router.post("", status_code=status.HTTP_201_CREATED)
async def post_one_offer(offer: OfferDetails):
    print(offer.listingOfferId)

    listingObj = await ListingDetails.get(offer.listingOfferId)
    
    print(listingObj)
    result = await offer.insert()    

    print(result.id)
    await listingObj.update({'$push': {'listingOfferIds':str(result.id)}})

    return result

# FOR ALL PATCHES, CHECK IF ID WAS PROVIDED TO ERROR HANDLE PROPERLY
# EXTRA CHECKS IN PLACE FOR CONTROLLLING NOT TO UPDATE THE LISTING GAME ON PUT/PATCH

@router.put("", status_code=status.HTTP_201_CREATED)
async def put_one_offer(offer: OfferDetails):
    result = await offer.replace()
    return result

@router.patch("", status_code=status.HTTP_201_CREATED)
async def patch_one_offer(offer: OfferDetails):
   document_dict = {}
   print(offer.model_dump().items())
   for key, value in offer.model_dump().items():
       print(value)
       if value is not None:
           document_dict[key] = value
   print(document_dict)
   result = await offer.update({'$set': document_dict})
   return result

@router.delete("/{offer_id}", status_code=status.HTTP_200_OK)
async def delete_one_offer(offer_id):
    offer = await OfferDetails.get(offer_id)
    print(offer)

    listingObj = await ListingDetails.get(offer.listingOfferId)

    result = await listingObj.update({'$pull': {'listingOfferIds':offer_id}})
    print(result)

    await offer.delete()
    return {}