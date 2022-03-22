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
# TODO::: implement movies data model

# TODO::: implement actors data model
