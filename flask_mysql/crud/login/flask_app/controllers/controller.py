from flask_app import app
from flask import render_template, redirect, request, session
# import the class from friend.py
from flask_app.models.****modelname**** import ****classname****

@app.route('/')
def index():