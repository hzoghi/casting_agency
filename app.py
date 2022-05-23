# imports
# -------------------------------------------------------- #
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

# app initiation and database setup
# -------------------------------------------------------- #
app = Flask(__name__)
# CORS(app)
# app.config.from_object('config')
# moment = Moment(app)
# db = SQLAlchemy(app)
#
# migrate = Migrate(app. db)


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


# setup_db(app)
# db_drop_and_create_all()

# endpoints
# -------------------------------------------------------- #

# TODO::: Implement GET/actors and /movies
# TODO::: Implement DELETE/actors and /movies
# TODO::: Implement POST/actors and /movies
# TODO::: Implement PATCH /actors and /movies

@app.route('/')
def test():
    return 'hello'

if __name__ == '__main__':
    app.run()
