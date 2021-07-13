from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    session["name"]=request.form['name']
    session["language"]=request.form['language']
    session["location"]=request.form['location']
    session["comment"]=request.form['comment']
    print(session["name"])
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], comment=session["comment"],
    language=session["language"], location = session["location"] )

@app.route('/back', methods=['post'])
def back():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)