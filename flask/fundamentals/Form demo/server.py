from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "jon"


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template("from_form.html", name = session['name'], email = session['email'])

@app.route('/destroy')
def destroy():
    pass
if __name__ == "__main__":
    app.run(debug=True)

