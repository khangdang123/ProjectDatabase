# Import 'os' module
import os

# Establish a base directory for constructing file paths in a Flask application.
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration Settings
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'NoteApp'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


