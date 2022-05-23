# Data Models
# Imports
#from app import db
# from flask_sqlalchemy import SQLAlchemy
# -------------------------------------------------------- #


# utilities
# -------------------------------------------------------- #



# tables
# -------------------------------------------------------- #
association_table = db.Table('association',
                             db.Column('movie_id', db.ForeignKey('movie.id'), primary_key=True),
                             db.Column('actor_id', db.ForeignKey('actor.id'), primary_key=True))


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    actors = db.relationship('Actor')


class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
