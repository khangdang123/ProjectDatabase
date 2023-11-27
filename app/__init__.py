# Import all the modules that we need to initialize in this project: 
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Create an instance of Flask class,
app = Flask(__name__)

# Create a location for a database to located.
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'NoteApp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize a SQLAlchemy database with the setting from the Flask application
db = SQLAlchemy(app)

# Establish a migration framework, linking to the Flask application and database
migrate = Migrate(app, db)

# Initialize a LoginManager for the Flask application
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
