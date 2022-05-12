from operator import contains
from flask import Flask, redirect, url_for, request, jsonify
from dynamicModel import Game, db
from staticModel import GAMES, getGameById

#to see the result type "flask run" into the terminal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)


@app.route('/')#<-- called "Decorator"
def home():
    return 'You are now home. Please read the instructions in Readme.txt file'


@app.route('/allgames')
def allgames(): #<-- create a dictonary using JSON method/format (in postman use localhost5000:/allgames to access the dictionary)
    data = Game.query.all()
    if 'list' not in type(data):
        games = []
        for p in data:
            games.append(p.to_dict())
        else:
            games.append(data.to_dict())

    games = {
        'games' : games
    }
    return games

@app.route('/allgames', methods=['POST'])
def create_game():
    f_id = request.form['id']
    f_name = request.form['name']
    f_price = request.form['price']
    to_add = Game(id=f_id, name=f_name, price=f_price)
    db.session.add(to_add)
    db.session.commit()
    return redirect(url_for('allgames'))

@app.route('/allgames/<id>')
def gameByRoute(id):
    result = getGameById(int(id))
    if result:
        return result
    else:
        return{"error":"No potion with that ID found."}


'''
# using parameter
@app.route('/games')
def gameByParam():
    id = request.args['id']
    result = getGameById(int(id))
    if result:
        return result
    else:
        return{"error":"No potion with that ID found."}

#using JSON
@app.route('/games', methods=['POST'])
def potionByPost():
    id = request.json['id']
    result = getGameById(int(id))
    if result:
        return result
    else:
        return{"error":"No game with that ID found."}

@app.route('/allgames/<catagory>/<id>')
def lookupGameByRoute(catagory,id):
    if catagory.lower() == 'genre':
        result = getGameById(int(id))
        if result:
            return result
        else:
            return {"error":f"{id} is not a valid id {catagory}"}
    else:
        return {"error":f"{id} is not a valid id {catagory}"}
'''