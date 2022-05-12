from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    genre = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.id}:{self.name}\tgenre:{self.genre}'

    def to_dict(self):
        return {'id':self.id, 'name':self.name, 'genre':self.genre}

