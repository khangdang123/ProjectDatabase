from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_bootstrap import Bootstrap

# Create an instance of Flask class,
app = Flask(__name__)

# Create a location for a database to located.
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'note app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Configure things we need to let 1 gmail account automatically send password reset link to users:
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


# Initialize a SQLAlchemy database with the setting from the Flask application
db = SQLAlchemy(app)

# Establish a migration framework, linking to the Flask application and database
migrate = Migrate(app, db)

# Initialize a LoginManager for the Flask application
login = LoginManager(app)
login.login_view = 'login'

bootstrap = Bootstrap(app)

from app import routes, models
