from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_ninja(cls, data):
        query = 'insert into ninjas(first_name, last_name, age, dojo_id) VALUES ( %(fname)s, %(lname)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data) 