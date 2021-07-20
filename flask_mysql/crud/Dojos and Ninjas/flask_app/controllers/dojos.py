from flask_app import app
from flask import render_template, redirect, request
# import the class from friend.py
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    dojos=Dojo.get_all_dojos()
    print(dojos)
    return render_template('index.html', all_dojos = dojos)

@app.route('/form')
def newForm():
    dojos=Dojo.get_all_dojos()
    print(dojos)
    return render_template('form.html', all_dojos = dojos)

@app.route('/createNinja', methods=["POST"])
def createNinja():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id'],
    }
    id = data['dojo_id']
    Ninja.add_ninja(data)
    return redirect('/dojos/'+str(id))

@app.route('/createDojo', methods=["POST"])
def createDojo():
    data = {
        'dname': request.form['dname'],
    }
    Dojo.add_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:id>')
def get_students(id):
    data = {
        'id':id
    }
    students=Dojo.get_all_students(data)

    if (students == ()):
        return redirect('/')

    print(students)
    return render_template('dojo.html', all_students = students) 