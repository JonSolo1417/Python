from flask import Flask, app, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all_users()
    print(users)
    return render_template('index.html' , all_users = users)

@app.route('/form')
def form():
    return render_template('create.html')

@app.route('/create', methods=["POST"])
def create():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'eml': request.form['eml']
    }
    User.add_user(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
