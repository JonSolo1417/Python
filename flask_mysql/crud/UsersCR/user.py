from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_At = data['created_at']
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