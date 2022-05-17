from flask_app.config.myslqconnection import connectToMySQL
from flask import flash

class Party:
    db_name = 'HotGirlParties'
    def __init__( self , data ):
        self.id = data['id']
        self.starttime = data['starttime']
        self.endtime = data['endtime']
        self.genre = data['genre']
        self.instructor = data['instructor']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO parties ( starttime , endtime, genre, user_id, created_at, updated_at) VALUES ( %(starttime)s , %(endtime)s , %(genre)s , %(user_id)s, NOW() , NOW());"
        result = connectToMySQL(cls.db_name).query_db( query, data )
        return result

    @classmethod
    def saved(cls, data):
        query = "INSERT INTO parties ( starttime , endtime, genre, created_at, updated_at) VALUES ( %(starttime)s , %(endtime)s , %(genre)s , NOW() , NOW());"
        result = connectToMySQL(cls.db_name).query_db( query, data )
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE parties SET starttime=%(starttime)s, endtime=%(endtime)s, genre=%(genre)s, user_id=%(user_id)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def updated(cls, data):
        query = "UPDATE parties SET starttime=%(starttime)s, endtime=%(endtime)s, genre=%(genre)s,user_id= null, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT users.username as instructor, parties.* FROM parties LEFT JOIN users on users.id=parties.user_id"
        results = connectToMySQL(cls.db_name).query_db(query)
        parties = []
        for party in results:
            parties.append( cls(party) )
        return parties

    @classmethod
    def get_upcoming(cls):
        query = "SELECT users.username as instructor, parties.* FROM parties LEFT JOIN users on users.id=parties.user_id Where starttime > NOW() ORDER BY starttime;"
        results = connectToMySQL(cls.db_name).query_db(query)
        parties = []
        for party in results:
            parties.append( cls(party) )
        return parties

    @classmethod
    def get_one(cls,data):
        query = "SELECT users.username as instructor, parties.* FROM parties LEFT JOIN users on users.id=parties.user_id WHERE parties.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def take(cls, data):
        query = "UPDATE parties SET user_id=%(user_id)s , updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM parties WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_party(party):
        is_valid = True
        if party['starttime'] == "":
            flash("Please select a start time")
            is_valid = False
        if party['endtime'] == "": 
            flash("Please select an end time")
            is_valid = False
        return is_valid