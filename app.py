# imports
# -------------------------------------------------------- #
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db_drop_and_create_all, setup_db

# app initiation and database setup
# -------------------------------------------------------- #
app = Flask(__name__)
migrate = Migrate()
CORS(app)

setup_db(app)
db_drop_and_create_all()

#endpoints
# -------------------------------------------------------- #

# TODO::: Implement GET/actors and /movies
# TODO::: Implement DELETE/actors and /movies
# TODO::: Implement POST/actors and /movies
# TODO::: Implement PATCH /actors and /movies
