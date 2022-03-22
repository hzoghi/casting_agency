# imports
import os

# -------------------------------------------------------- #
SQLALCHEMY_DATABASE_URI = 'postgres://hamed.zoghi@localhost:5432/casting'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
database_filename = "database.db"

DEBUG = True
