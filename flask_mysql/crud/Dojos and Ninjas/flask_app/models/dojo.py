from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query= 'select * from dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        print(dojos)
        return dojos

    @classmethod
    def add_dojo(cls, data):
        query = 'insert into dojos(name) VALUES ( %(dname)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_all_students(cls, data):
        query = 'select ninjas.first_name, ninjas.last_name, ninjas.age,dojos.name from dojos join ninjas on dojos.id =ninjas.dojo_id where dojo_id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)