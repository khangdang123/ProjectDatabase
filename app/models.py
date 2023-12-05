import jwt
from app import db, login, app
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from time import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Set up the User table in Database
class User(UserMixin, db.Model):
   # User's ID(Primary Key)
   id = db.Column(db.Integer, primary_key=True)
   # User's username
   username = db.Column(db.String(64), index=True, unique=True)
   # User's email
   email = db.Column(db.String(120), index=True, unique=True)
   # User's password
   password_hash = db.Column(db.String(128))

   # Set up relation with class Post
   posts = db.relationship('Post', backref='author', lazy='dynamic')

   # Function which generates a hash for the given password(Secure Password)
   def set_password(self, password):
       self.password_hash = generate_password_hash(password)

   # Function which check the hash of passwork given by user and the password was stored in Database
   def check_password(self, password):
       return check_password_hash(self.password_hash, password)

   # Function that returns a string representing the object.
   def __repr__(self):
       return '<User {}>'.format(self.username)



# Set up the Post table in Database
class Post(db.Model):
   # Post ID
   id = db.Column(db.Integer, primary_key=True)
   # Post Body
   body = db.Column(db.String(140))
   # Post timestamp
   timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   # Set up relationship with the class User
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

   # Function that returns a string representing the object.
   def __repr__(self):
       return '<Post {}>'.format(self.body)

# Load a user based on their ID, and it retrieves the user from the database using SQLAlchemy. 
@login.user_loader
def load_user(id):
   return User.query.get(int(id))

# Set up the Comment Table in Database
class Comment(db.Model):
   # Note's id
   id = db.Column(db.Integer, primary_key=True)
   # Note text
   text = db.Column(db.String(255), nullable=False)
   # Time stamp
   timestamp = db.Column(db.DateTime, default=datetime.utcnow)
   # Set up relationship with the class Note
   note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

# Set up the Note Table in Database
class Note(db.Model):
   # Note's ID
   id = db.Column(db.Integer, primary_key=True)
   # Note's title
   title = db.Column(db.String(120), nullable=False)
   # Note's content
   content = db.Column(db.String(255), nullable=False)  
   # Set up relation with class Comment
   comments = db.relationship('Comment', backref='note', lazy='dynamic')

   # Function that returns a string representing the object.
   def __repr__(self):
       return f'<Note {self.id}: {self.title}>'




