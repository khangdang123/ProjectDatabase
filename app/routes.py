from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from werkzeug.urls import url_parse
from app import db

@app.route('/')
def home():
    return render_template('home.html')
