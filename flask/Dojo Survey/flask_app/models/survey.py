from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_survey(cls,data):
        query = ' insert into dojos (name,location,language,comment) values(%(nme)s,%(loc)s,%(lang)s,%(cmnt)s);'
        return connectToMySQL('dojo_survey').query_db(query,data)
    
    @classmethod
    def return_survey(cls,data):
        query = 'select * from dojos where dojos.id = %(id)s'
        return connectToMySQL('dojo_survey').query_db(query,data)
    
    @classmethod
    def get_survey(cls,data):
        query = 'select * from dojos where id = %(id)s'
        result = connectToMySQL('dojo_survey').query_db(query,data)
        print (result)
        return cls(result[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['nme']) < 1:
            flash('Name field must not be empty.')
            is_valid= False
        if (survey['loc']) =='Choose a Dojo':
            flash('Must select a dojo.')
            is_valid= False
        if (survey['lang']) == 'Select your favorite language':
            flash('Must select a favorite language.')
            is_valid= False
        return is_valid

