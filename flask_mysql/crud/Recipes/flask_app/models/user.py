from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

from flask import flash

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']

    @classmethod
    def check_email(cls,data):
        query = 'select * from users where email = %(email)s;'
        result = connectToMySQL('recipes').query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def add_user(cls,data):
        query='insert into users (first_name,last_name,email,password) values (%(first_name)s,%(last_name)s,%(email)s,%(password)s)'
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod 
    def one_user(cls,data):
        query='select * from users where id = %(id)s;'
        result = connectToMySQL('recipes').query_db(query,data)
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash('First name field must have at least 2 characters.')
            is_valid= False
        if len(user['last_name']) < 1:
            flash('Last name field must have at least 2 characters.')
            is_valid= False
        if len(user['email']) < 1:
            flash('Email field must not be empty.')
            is_valid= False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 5:
            flash('Password must be 5 characters')
            is_valid= False
        if user['password'] !=  user['confirm']:
            flash('Passwords do not match')
            is_valid= False
        return is_valid
