from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "select * from users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls, data):
        query = 'insert into users(first_name, last_name, email) VALUES ( %(fname)s , %(lname)s ,%(eml)s);'
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def get_one_user(cls, data):
        query = "select * from users where id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def edit_user(cls, data):
        query = 'update users_schema.users set first_name = %(fname)s,last_name = %(lname)s, email = %(eml)s where id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete_user(cls, data):
        query = 'delete from users where id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query,data)

