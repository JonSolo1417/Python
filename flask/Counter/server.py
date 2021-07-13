from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    return redirect('/visit')

@app.route('/visit')
def visit():
    session['visits'] += 1
    return render_template("index.html", visits_on_template=session['visits'])

@app.route('/plus2', methods=['post'])
def plus2():
    session['visits'] += 1
    return redirect('/visit')

@app.route('/destroy', methods=['post'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)