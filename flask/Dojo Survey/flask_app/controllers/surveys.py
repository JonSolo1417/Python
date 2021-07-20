from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.survey import Survey



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    data = {
        'nme' : request.form['nme'],
        'loc' : request.form['loc'],
        'lang' : request.form['lang'],
        'cmnt' : request.form['cmnt']
    }
    if not Survey.validate_survey(request.form):
        return redirect('/')
    id = Survey.add_survey(data)
    print (id)
    return redirect('/result/'+str(id))

@app.route('/result/<int:id>')
def result(id):
    data = {
        'id':id
    }
    survey=Survey.get_survey(data)
    return render_template('result.html', survey=survey)

@app.route('/back', methods=['post'])
def back():
    session.clear()
    return redirect('/')