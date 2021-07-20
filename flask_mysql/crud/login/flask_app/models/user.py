from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

from flask import flash

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)    

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_user(cls,data):
        query = 'insert into user (first_name,last_name,email,password) values (%(fname)s,%(lname)s,%(mail)s,%(pass)s)'
        return connectToMySQL('login_registration').query_db(query,data)

    @classmethod
    def check_email(cls,data):
        query = 'select * from user where email = %(email)s;'
        result = connectToMySQL('login_registration').query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['fname']) < 1:
            flash('First name field must not be empty.')
            is_valid= False
        if len(user['lname']) < 1:
            flash('Last name field must not be empty.')
            is_valid= False
        if len(user['mail']) < 1:
            flash('Email field must not be empty.')
            is_valid= False
        if len(user['pass']) < 8:
            flash('Password must be 8 characters')
            is_valid= False
        return is_valid