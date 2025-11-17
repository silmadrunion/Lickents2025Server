from fastapi import APIRouter, status

from typing import Union

from models.game import GameObject, GameDetails
from models.user import UserDetails, default_user

router = APIRouter(prefix="/game")

@router.get("", status_code=status.HTTP_200_OK)
async def get_all_games(user_id: Union[str, None] = None):
    if user_id:
        print("User Query Parameter provided: ", user_id)
        #gameObj = await handler.get_multiple_from_collection({"gameOwnerId": user_id}) #Recheck sometime
        gameObj = await GameDetails.find({"gameOwnerId": user_id}).to_list()

    else:
        gameObj = await GameDetails.find().to_list()
    print("DB RESULT:", gameObj)
    for item in gameObj:
        item = GameObject(gameUserDetails=default_user, gameDetails=item)
    print(gameObj)
    return gameObj

@router.get("/{game_id}", status_code=status.HTTP_200_OK)
async def get_game_by_id(game_id):
    print(game_id)
    #gameObj = await handler.get_from_collection(game_id)

    result = await GameDetails.get(game_id)

    print("DB RESULT:", result)

    gameObj = GameObject(gameUserDetails = default_user, gameDetails = result)

    print(gameObj)
    return gameObj

@router.post("", status_code=status.HTTP_201_CREATED)
async def post_one_game(game: GameDetails):
    result = await game.insert()
    return result

@router.put("", status_code=status.HTTP_201_CREATED)
async def put_one_game(game: GameDetails):
    result = await game.replace()
    return result

@router.patch("", status_code=status.HTTP_201_CREATED)
async def patch_one_game(game: GameDetails):
   document_dict = {}
   for key, value in game.model_dump().items():
       if value is not None:
           document_dict[key] = value
   result = await game.update({'$set': document_dict})

@router.delete("/{game_id}", status_code=status.HTTP_200_OK)
async def delete_one_game(game_id):
    game = await GameDetails.get(game_id)
    print(game)
    await game.delete()
    return {}