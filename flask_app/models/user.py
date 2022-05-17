from sqlite3 import connect
from threading import stack_size
from flask_app.config.myslqconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name = 'HotGirlParties'
    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.level = data['level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( username , email , password, level, created_at, updated_at ) VALUES ( %(username)s , %(email)s , %(password)s, %(level)s, NOW() , NOW() );"
        result = connectToMySQL(cls.db_name).query_db( query, data )
        return result

    @classmethod
    def get_by_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_instructors(cls):
        query = "SELECT * from users WHERE level = 2;"
        results = connectToMySQL(cls.db_name).query_db(query)
        instructors = []
        for instructor in results:
            instructors.append( cls(instructor) )
        return instructors

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * from users WHERE username = %(username)s;"
        results = connectToMySQL(User.db_name).query_db(query, user)
        if len(results) >=1:
            flash("Username already taken")
            is_valid = False
        if len(user['username']) < 2:
            flash("Username must be at least 2 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        if user['password'] != user['cpassword']:
            flash("Passwords must match")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not user['level']:
            flash("Please select a role")
            is_valid = False
        return is_valid