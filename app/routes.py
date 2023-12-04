from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm, RegistrationForm, CreateNote, EditNoteForm, CommentForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Note, Comment
from werkzeug.urls import url_parse
from app import db
import json, requests

# Create an array for variable 'notes'
notes = []

@app.route('/')
def home():
   # Renders the 'home.html' template when users in the Root URL.
   return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
   # Check if the current user is authenticated(Check username and password) and redirect the user to the index page
   if current_user.is_authenticated:
       return redirect(url_for('index'))
   # Create an instance of the LoginForm
   form = LoginForm()

   # If the form has been submitted with all fields are filled, attempt to log in
   if form.validate_on_submit():
       # Query the User Table for a user with the specified name.
       user = User.query.filter_by(username=form.username.data).first()
       # If the user doesn't exist or the user enterting invalid password of the account
       if user is None or not user.check_password(form.password.data):
           # Print message
           flash('Invalid username or password')
           # Redirect to login page
           return redirect(url_for('login'))
       # If the user exist and entered valid password, redirect to index page
       login_user(user, remember=form.remember_me.data)
       return redirect(url_for('index'))
   # Renders the 'login.html' template when users in the login page
   return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
   # Log out the user and redirect user to login page
   logout_user()
   return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
   # Check if the current user is authenticated(Check username and password) and redirect the user to the index page
   if current_user.is_authenticated:
       return redirect(url_for('index'))
   # Create an instance of the RegistrationForm
   form = RegistrationForm()
   # If the form has been submitted and is valid
   if form.validate_on_submit():
       # Create a new User object with the data in the form and add it to the database
       user = User(username=form.username.data, email=form.email.data)
       user.set_password(form.password.data)
       db.session.add(user)
       db.session.commit()
       # Print message if success
       flash('Congratulations, you are now a registered user!')
       # Redirect to the login page after created the account
       return redirect(url_for('login'))
   # Renders the 'register.html' template when users in the register page
   return render_template('register.html', title='Register', form=form)

@app.route('/index')
def index():
   # Create the database tables if they do not exist
   db.create_all()
   # Query all notes from the Note model
   notes = Note.query.all()
   # Call the function load_notes
   load_notes()
   # Renders the 'index.html' template when users in the index page
   return render_template('index.html',notes=notes)


@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
   # Create an instance of the CreateNote form
   form = CreateNote()

   # If the form has been submitted and is valid
   if form.validate_on_submit():
       # Extract the data from the form
       title = form.title.data
       note_content = form.note.data

       # Create a new instance of the Note model with the form data
       new_note = Note(title=title, content=note_content)

       # Add and commit new note to the database
       db.session.add(new_note)
       db.session.commit()

       # Print message
       flash('Note created successfully!', 'success')
       # Redirect to the index page after creating the note
       return redirect(url_for('index'))

   # Renders the 'create.html' template if form has not been submitted
   return render_template('create.html', title='Create Note', form=form)


@app.route('/delete_note/<int:id>', methods=['GET','POST'])
def delete_note(id):
   # Check if the request method is POST
   if request.method == 'POST':
       # Retrieve the note with the specified ID or return a 404 error if not found
       note_to_delete = Note.query.get_or_404(id)

       # Delete the note from the database
       db.session.delete(note_to_delete)
       # Commit the change of notes to the database
       db.session.commit()
   # Redirect to the index page after deleted the note
   return redirect(url_for('index'))


def load_notes():
   # Use the 'global' keyword to access the 'notes' variable outside the function
   global notes
   try:
       # Try to open and read the 'notes.json' file
       with open('notes.json', 'r') as file:
           # Attempt to load JSON data from the file
           notes = json.load(file)
   except (FileNotFoundError, json.JSONDecodeError):
       notes = []
   #  Return the loaded notes
   return notes


@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
   # Query the note with the specified ID from the database
   note = Note.query.get(note_id)

   # If note doesn't exist, print message
   if not note:
       return "Note not found", 404

   # Create an instance of the EditNoteForm
   form = EditNoteForm(obj=note)

   # Check if the request method is POST and the form is valid
   if request.method == 'POST' and form.validate_on_submit():
       # Update the note object with the form data
       form.populate_obj(note)

       # Commit the changes to the database
       db.session.commit()

       # Print message if note updated succesfully
       flash('Note updated successfully!', 'success')
       # Redirect to the index page after updating the note
       return redirect(url_for('index'))

   # Render the 'edit_note.html' template with the form and note data
   return render_template('edit_note.html', form=form, note=note)

@app.route('/index/', methods=['GET', 'POST'])
def sort():
   # Create the database tables if they do not exist
   db.create_all()
   # Query all notes from the Note model
   notes = Note.query.all()

   # If the request method is POST
   if request.method == 'POST':
       # if the 'sort_button' is present in the form data
       if 'sort_button' in request.form:
           # Retrieve the selected sort option from the form data
           sort_option = request.form['sort_option']

           # Perform sorting based on the selected option
           if sort_option == 'title':
               notes = sorted(notes, key=lambda x: x.title)
           elif sort_option == 'content':
               notes = sorted(notes, key=lambda x: x.content)
           elif sort_option == 'id':
               notes = sorted(notes, key=lambda x: x.id)

   # Render the 'index.html' template with the sorted notes
   return render_template('index.html', notes=notes)


@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def show_detail(note_id):
   #Query the note with the specified ID from the database
   note = Note.query.get(note_id)

   # if the note exists
   if not note:
       return "Note not found", 404

   # Create an instance of the CommentForm
   comment_form = CommentForm()  

   # If the request method is POST and the comment form is valid
   if request.method == 'POST' and comment_form.validate_on_submit():
       # Create a new comment associated with the current note
       new_comment = Comment(text=comment_form.text.data, note=note)
       # Add the new comment to the database
       db.session.add(new_comment)
       # Commit the new comment to the database
       db.session.commit()
       # Print message if comment added successfully
       flash('Comment added successfully!', 'success')

   # Render the 'note.html' template with the note and comment form data
   return render_template('note.html', note=note, comment_form=comment_form)

@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        search_term = request.form.get('search_term', '')
    else:
        search_term = request.args.get('search_term', '')

    params = {
        'access_key': 'cf3b6b3d28b18a7f0b380d7a89b5ea30',
        'countries': 'us',
        'sort': 'published_desc',
        'keywords': search_term,
    }

    response = requests.get(MEDIASTACK_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = parse_articles(data)
        return render_template('news.html', articles=articles, search_term=search_term, notes=notes)

def parse_articles(data):
    articles = []
    counter = 0

    while len(articles) < 4 and counter < len(data.get("data", [])):
        if "image" in data["data"][counter] and data["data"][counter]["image"]:
            author = data["data"][counter]["author"]
            title = data["data"][counter]["title"]
            img = data["data"][counter]["image"]
            url = data["data"][counter]["url"]
            article = {"author": author, "title": title, "img": img, "url": url}
            articles.append(article)
        counter += 1

    return articles
