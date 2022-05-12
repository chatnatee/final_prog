GAMES = [
            {
                "id":0,
                "name":"healing potion",
                "genre": 200
            },
            {
                "id":1,
                "name":"speed potion",
                "genre": 500
            },
            {
                "id":2,
                "name":"polymorph potion",
                "genre": 5000
            }
]

def getAllGames():
    return GAMES

def getGameById(id):
    for game in GAMES:
        if game['id'] == id:
            return game
    return None


