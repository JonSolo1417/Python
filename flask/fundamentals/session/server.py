from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# our index route will handle rendering our form
@app.route('/')
def index():

    if 'total' not in session:
        session['total'] = 0

    session['total'] += 1

    return render_template("index.html")



@app.route('/success')
def success():
    if 'name' not in session:
        session['name'] = "Had to give this a real name!"
    if 'email' not in session:
        session['email'] = "Email was never supplied, spider got me down"

    return render_template('from_form.html', name_on_template=session['name'], email_on_template=session['email'])


@app.route('/check')
def check():
    return render_template('from_form.html')




@app.route('/users', methods=['post'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.

    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # session['user'] = request.form['user']
    session['spider'] = request.form['spider']
    session['desc'] = request.form['desc']


    return redirect('/success')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
