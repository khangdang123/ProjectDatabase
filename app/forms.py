from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed
from app.models import User

# User Login form for accessing their account
class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')

# User registration form for the new users.
class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired()])
   password2 = PasswordField(
       'Repeat Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Register')

# Custom validation method for username uniqueness
   def validate_username(self, username):
       user = User.query.filter_by(username=username.data).first()
       if user is not None:
           raise ValidationError('Please use a different username.')

# Custom validation method for email uniqueness
   def validate_email(self, email):
       user = User.query.filter_by(email=email.data).first()
       if user is not None:
           raise ValidationError('Please use a different email address.')


# Create Note form
class CreateNote(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   note = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=500)])
   attachment = FileField('Attachment', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'pdf'])])
   submit = SubmitField('Save')


# Edit Note form
class EditNoteForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   content = TextAreaField('Content', validators=[DataRequired()])


# Comment Note form
class CommentForm(FlaskForm):
   text = StringField('Comment', validators=[DataRequired()])
   submit = SubmitField('Add Comment')

# ReName form
class ReTitleForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   content = TextAreaField('Content', validators=[DataRequired()])

# Reset Password form
class ResetPasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Reset Password')
