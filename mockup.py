deleted_empty = '''
                {
                }
    '''

# Conversation: a game's structure should have some basic info outside of all nesting, such as _id, userId, possibly Name ; a gameUserDetails with full user details ; and a gameDetails with full game details
# In regards to POST: POST (and consequently PUT and PATCH) will need to format their data to include the gameDetails key themselves, and not just send all data unformatted then expect the GET to be formatted by the DB

all_games = '''[

    {
        "gameId":"1231231231",
        "gameOwnerId":"stri123123123ng",
        "gameImagePath":"string",
        "gameName":"Ark Nova (2021)",
        "gameDetails":{
            "gameDescription":"Plan and build a modern, scientifically managed zoo to support conservation projects.",
            "gamePlayerNo":"1 - 4",
            "gameReccommandedAge":"14+",
            "gamePlayTime":"90 - 150  Min",
            "gameComplexity":3.33,
            "gameBGGRating":8.5
        }
    },
    {
        "gameId":"1231231231",
        "gameOwnerId":"stri123123123ng",
        "gameImagePath":"string",
        "gameName":"Ark Nova (2021)",
        "gameDetails":{
            "gameDescription":"Plan and build a modern, scientifically managed zoo to support conservation projects.",
            "gamePlayerNo":"1 - 4",
            "gameReccommandedAge":"14+",
            "gamePlayTime":"90 - 150  Min",
            "gameComplexity":3.33,
            "gameBGGRating":8.5
        }
    }

]'''

single_game = '''{

    "gameId":"1231231231",
    "gameOwnerId":"stri123123123ng",
    "gameClientRating":4.99,
    "gameClientName":"Fluff Robota ",
    "gameClientImagePath":"string",
    "gameClientDescription":"Game is in great condition. Basically new. I have played it once or twice and it seems too complex for me and my friends.",
    "gameClientImagesProvided":true,
    "gameImagePath":"string",
    "gameName":"Ark Nova (2021)",
    "gameDescription":"Plan and build a modern, scientifically managed zoo to support conservation projects.",
    "gamePlayerNo":"1 - 4",
    "gameReccommandedAge":"14+",
    "gamePlayTime":"90 - 150  Min",
    "gameComplexity":3.33,
    "gameBGGRating":8.5,
    "gameDesigners":[
        "Action Queue",
        "End Game Bonuses"
    ],
    "gameArtists":[
        "Action Queue",
        "End Game Bonuses"
    ],
    "gameMechanisms":[
        "Action Queue",
        "End Game Bonuses",
        "Grid Coverage",
        "Hand Management"
    ],
    "gameCategories":[
        "Action Queue",
        "End Game Bonuses",
        "Grid Coverage",
        "Hand Management"
    ]

}'''

single_listing = '''{
    "listingId" : "mockListingId",
    "gameId" : "mockGameId",
    "userId" : "mockUserId",
    "gameDetails" : {
        "gameName" : "Mock Game Name",
        "otherDetails" : "This data comes from the Games DB entity, actually, but I'll return it through the Listing endpoint for frontend purposes"
    },
    "offers" : [ 
    {
    "offerId" : "mockOfferId1",
    "offerUserId" : "mockOfferUID1",
    "offerDetails" : {
        "someDetails" : "Probably some array of games that contain simple game info on each, like game name, coming from the Games DB Entity once again",
        "chatData" : "Chat data probably lives here. If not, a chat data ID will still certainly live here"
        }
    },
    {
    "offerId" : "mockOfferId2",
    "offerUserId" : "mockOfferUID2",
    "offerDetails" : {
        "someDetails" : "Probably some array of games that contain simple game info on each, like game name, coming from the Games DB Entity once again",
        "chatData" : "Chat data probably lives here. If not, a chat data ID will still certainly live here"
        }
    }
    ]
}'''

all_listings = '''[
    {
    "listingId" : "mockListingId1",
    "gameId" : "mockGameId",
    "userId" : "mockUserId",
    "gameDetails" : {
        "gameName" : "Mock Game Name One",
        "otherDetails" : "This data comes from the Games DB entity, actually, but I'll return it through the Listing endpoint for frontend purposes"
    }
    },
    {
    "listingId" : "mockListingId2",
    "gameId" : "mockGameId",
    "userId" : "mockUserId",
    "gameDetails" : {
        "gameName" : "Mock Game Name Two",
        "otherDetails" : "This data comes from the Games DB entity, actually, but I'll return it through the Listing endpoint for frontend purposes"
    }
    }
]'''

single_offer = '''{
    "offerId" : "mockOfferId",
    "userId" : "mockUserId",
    "listingGameDetails" : 
        {      
            "listingId" : "mockListingId",
            "otherDetails" : "Some Listing data returned here to be able to display on offers screen"
        },
    "offerGamesDetails" : [
        {
            "gameId" : "mockGameId1",
            "gameName" : "Mock Game Name One",
            "otherDetails" : "all relevant game detail data"
        },
        {
            "gameId" : "mockGameId2",
            "gameName" : "Mock Game Name Two",
            "otherDetails" : "all relevant game detail data"
        }
    ]
}'''

all_offers = '''[
{
    "offerId" : "mockOfferId1",
    "userId" : "mockUserId",
    "listingGameDetails" : 
        {      
            "listingId" : "mockListingId",
            "otherDetails" : "Some Listing data returned here to be able to display on offers screen"
        },
    "offerGamesDetails" : [
        {
            "gameId" : "mockGameId1",
            "gameName" : "Mock Game Name One",
            "otherDetails" : "all relevant game detail data ; for ALL endpoint, perhaps stripped down"
        },
        {
            "gameId" : "mockGameId2",
            "gameName" : "Mock Game Name Two",
            "otherDetails" : "all relevant game detail data"
        }
    ]
},
{
    "offerId" : "mockOfferId2",
    "userId" : "mockUserId",
    "listingGameDetails" : 
        {      
            "listingId" : "mockListingId",
            "otherDetails" : "Some Listing data returned here to be able to display on offers screen"
        },
    "offerGamesDetails" : [
        {
            "gameId" : "mockGameId1",
            "gameName" : "Mock Game Name One",
            "otherDetails" : "all relevant game detail data ; for ALL endpoint, perhaps stripped down"
        },
        {
            "gameId" : "mockGameId2",
            "gameName" : "Mock Game Name Two",
            "otherDetails" : "all relevant game detail data"
        }
    ]
}
]'''

game_post = '''
{
}
'''

game_put = '''
{
}
'''

game_patch = '''
{
}
'''

listing_post = '''
{
}
'''

listing_put = '''
{
}
'''

listing_patch = '''
{
}
'''

offer_post = '''
{
}
'''

offer_put = '''
{
}
'''

offer_patch = '''
{
}
'''