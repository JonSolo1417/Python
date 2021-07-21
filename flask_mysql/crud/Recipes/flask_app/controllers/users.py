
from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request, session
# import the class from friend.py
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def process_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash,
    }

    id=User.add_user(data)
    session['id']= id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not 'id' in session:
        flash("Please login to continue")
        return redirect('/')
    data= {
        'id' : session['id']
    }
    user = User.one_user(data)
    recipes = Recipe.get_recipes()
    print(recipes)
    return render_template('dashboard.html', user = user, recipes = recipes)

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
    return redirect("/dashboard")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add_recipe')
def new_recipe():
        if not 'id' in session:
            flash("Please login to continue")
            return redirect('/')
        return render_template('add_recipe.html')

@app.route('/process_recipe', methods = ['POST'])
def process_recipe():
    if not 'id' in session:
        flash("Please login to continue")
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/add_recipe')
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'under_30' : request.form['under_30'],
        'created_on' : request.form['created_on'],
        'user_id' : session['id'],
    }

    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/view/<int:id>')
def view_recipe(id):
        if not 'id' in session:
            flash("Please login to continue")
            return redirect('/')
        data = {
            'id' : session['id']
        }
        user = User.one_user(data)
        data = {
            'id':id
        }
        recipe =Recipe.get_recipe(data)
        print(recipe)
        return render_template('view.html',user = user, recipe=recipe)

@app.route('/delete/<int:id>')
def delete_recipe(id):
        if not 'id' in session:
            flash("Please login to continue")
            return redirect('/')
        data = {
            'id' : id
        }
        Recipe.delete_recipe(data)
        return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
        if not 'id' in session:
            flash("Please login to continue")
            return redirect('/')
        data = {
            'id' : id
        }
        recipe =Recipe.get_recipe(data)
        print(recipe)
        return render_template('edit.html',recipe=recipe)

@app.route('/edit/edit_recipe/<int:id>', methods=['POST'])
def edit_recipe(id):
        if not 'id' in session:
            flash("Please login to continue")
            return redirect('/')
        data = {
            'id':id,
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instructions' : request.form['instructions'],
            'under_30' : request.form['under_30'],
            'created_on' : request.form['created_on'],
            }
        recipe =Recipe.update_recipe(data)
        print('mad eit out of method')
        return redirect ('/view/'+str(id))