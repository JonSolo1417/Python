from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

from flask import flash

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.user_id = data['user_id']

    @classmethod
    def add_recipe(cls,data):
        query='insert into recipes (name,description,instructions,under_30,created_on, user_id) values (%(name)s,%(description)s,%(instructions)s,%(under_30)s,%(created_on)s,%(user_id)s);'
        return connectToMySQL('recipes').query_db(query,data)
    @classmethod
    def get_recipes(cls):
        query='select * from recipes;'
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        print(recipes)
        return recipes
    @classmethod
    def get_recipe(cls,data):
        query='select * from recipes where id = %(id)s;'
        results = connectToMySQL('recipes').query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete_recipe(cls,data):
        query='delete from recipes where id = %(id)s;'
        return connectToMySQL('recipes').query_db(query,data)
    
    @classmethod
    def update_recipe(cls,data):
        query='update recipes.recipes set name=%(name)s,description=%(description)s,instructions=%(instructions)s,under_30=%(under_30)s,created_on=%(created_on)s where id = %(id)s;'
        print ('made it to method')
        return connectToMySQL('recipes').query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('Name field must have at least 3 characters.')
            is_valid= False
        if len(recipe['description']) < 3:
            flash('Description field must have at least 3 characters.')
            is_valid= False
        if len(recipe['instructions']) < 3:
            flash('Instructions field must have at least 3 characters.')
            is_valid= False
        return is_valid