from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), index=True, unique=True)
   email = db.Column(db.String(120), index=True, unique=True)
   password_hash = db.Column(db.String(128))


   posts = db.relationship('Post', backref='author', lazy='dynamic')


   def set_password(self, password):
       self.password_hash = generate_password_hash(password)


   def check_password(self, password):
       return check_password_hash(self.password_hash, password)


   def __repr__(self):
       return '<User {}>'.format(self.username)


class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   body = db.Column(db.String(140))
   timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


   def __repr__(self):
       return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
   return User.query.get(int(id))


class Comment(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   text = db.Column(db.String(255), nullable=False)
   timestamp = db.Column(db.DateTime, default=datetime.utcnow)
   note_id = db.Column(db.Integer, db.ForeignKey('note.id'))


class Note(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(120), nullable=False)
   content = db.Column(db.String(255), nullable=False)  # Adjust the length as needed
   comments = db.relationship('Comment', backref='note', lazy='dynamic')
   def __repr__(self):
       return f'<Note {self.id}: {self.title}>'
