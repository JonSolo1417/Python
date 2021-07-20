from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request, session
# import the class from friend.py
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pass'])
    print(pw_hash)
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'mail' : request.form['mail'],
        'pass' : pw_hash
    }

    id=User.add_user(data)
    session['id']= id
    return redirect("/success")

@app.route('/success')
def success():
    if session['id']:
        return render_template('success.html')
    else:
        return redirect('/')

@app.route("/login", methods=['POST'])
def login():
    data = {'email':request.form['email']}
    in_db= User.check_email(data)

    if not in_db:
        flash('Invalid login credentials')
        return redirect("/")
    if not bcrypt.check_password_hash(in_db.password,request.form['password']):
        flash('Invalid login credentials')
        return redirect("/")
    session['id'] = in_db.id
    return redirect("/success")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')
    