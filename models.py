# Data Models
# Imports
import os
from flask_sqlalchemy import SQLAlchemy

# -------------------------------------------------------- #
database_filename = "database.db"
project_folder = os.path.dirname(os.path.abspath(__file__))
# TODO: database URI

# TODO: setup_db

db = SQLAlchemy()
