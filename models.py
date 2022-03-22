# Data Models
# Imports
from flask_sqlalchemy import SQLAlchemy

# -------------------------------------------------------- #
db = SQLAlchemy()


# utilities
# -------------------------------------------------------- #
def setup_db(app):
    """
    to setup database parameters
    :param app: Flask object
    :return: none
    """
    app.config.from_object('config')
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    """
    recreate the database
    :return: None
    """
    db.drop_all()
    db.create_all()


# tables
# -------------------------------------------------------- #
association_table = db.Table('association',
                             db.Column('movie_id', db.ForeignKey('movie.id')),
                             db.Column('actor_id', db.ForeignKey('actor.id')))


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    actors = db.relationship('Actor')


class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
