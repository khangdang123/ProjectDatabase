from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm, RegistrationForm, CreateNote, EditNoteForm, CommentForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Note, Comment
from werkzeug.urls import url_parse
from app import db
import json

notes = []


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
       return redirect(url_for('index'))
   form = LoginForm()
   if form.validate_on_submit():
       user = User.query.filter_by(username=form.username.data).first()
       if user is None or not user.check_password(form.password.data):
           flash('Invalid username or password')
           return redirect(url_for('login'))
       login_user(user, remember=form.remember_me.data)
       return redirect(url_for('index'))
   return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
   if current_user.is_authenticated:
       return redirect(url_for('index'))
   form = RegistrationForm()
   if form.validate_on_submit():
       user = User(username=form.username.data, email=form.email.data)
       user.set_password(form.password.data)
       db.session.add(user)
       db.session.commit()
       flash('Congratulations, you are now a registered user!')
       return redirect(url_for('login'))
   return render_template('register.html', title='Register', form=form)


@app.route('/index')
def index():
   db.create_all()
   notes = Note.query.all()
   load_notes()
   return render_template('index.html',notes=notes)





@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
   form = CreateNote()


   if form.validate_on_submit():
       title = form.title.data
       note_content = form.note.data


       # Assuming you have a Note model defined with title and content fields
       new_note = Note(title=title, content=note_content)


       db.session.add(new_note)
       db.session.commit()


       flash('Note created successfully!', 'success')
       return redirect(url_for('index'))


   return render_template('create.html', title='Create Note', form=form)


@app.route('/delete_note/<int:id>', methods=['GET','POST'])
def delete_note(id):
   if request.method == 'POST':
       note_to_delete = Note.query.get_or_404(id)


       db.session.delete(note_to_delete)
       db.session.commit()


   return redirect(url_for('index'))


def load_notes():
   global notes
   try:
       with open('notes.json', 'r') as file:
           notes = json.load(file)
   except (FileNotFoundError, json.JSONDecodeError):
       notes = []


   return notes


@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
   note = Note.query.get(note_id)


   if not note:
       return "Note not found", 404


   form = EditNoteForm(obj=note)


   if request.method == 'POST' and form.validate_on_submit():
       form.populate_obj(note)


       # Commit the changes to the database
       db.session.commit()


       flash('Note updated successfully!', 'success')
       return redirect(url_for('index'))


   return render_template('edit_note.html', form=form, note=note)


@app.route('/note/<int:note_id>')
def show_note(note_id):
   note = Note.query.get(note_id)
   if note:
       return render_template('note.html', note=note)
   else:
       return "Note not found", 404


@app.route('/index/', methods=['GET', 'POST'])
def sort():
   db.create_all()
   notes = Note.query.all()


   if request.method == 'POST':
       if 'sort_button' in request.form:
           sort_option = request.form['sort_option']


           if sort_option == 'title':
               notes = sorted(notes, key=lambda x: x.title)
           elif sort_option == 'content':
               notes = sorted(notes, key=lambda x: x.content)
           elif sort_option == 'id':
               notes = sorted(notes, key=lambda x: x.id)


   return render_template('index.html', notes=notes)

@app.route('/index/', methods=['GET', 'POST'])
def sort():
    db.create_all()
    notes = Note.query.all()

    if request.method == 'POST':
        if 'sort_button' in request.form:
            sort_option = request.form['sort_option']

            if sort_option == 'title':
                notes = sorted(notes, key=lambda x: x.title)
            elif sort_option == 'content':
                notes = sorted(notes, key=lambda x: x.content)

    return render_template('index.html', notes=notes)

@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def show_detail(note_id):
   note = Note.query.get(note_id)


   if not note:
       return "Note not found", 404


   comment_form = CommentForm()  # Create an instance of the CommentForm


   if request.method == 'POST' and comment_form.validate_on_submit():
       new_comment = Comment(text=comment_form.text.data, note=note)
       db.session.add(new_comment)
       db.session.commit()
       flash('Comment added successfully!', 'success')


   return render_template('note.html', note=note, comment_form=comment_form)