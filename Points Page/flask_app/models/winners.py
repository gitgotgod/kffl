from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

db = "winners"
class Winners:
    def __init__( self , data ):
        print("Data contents:", data)
        self.id = data['user_id']
        self.name = data['name']
        self.points = data['points']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        users_in_db = connectToMySQL(db).query_db(query)
        users_list = []
        for user in users_in_db:
            users_list.append(cls(user))
        return users_list
            
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (name, points, created_at, updated_at) VALUES (%(name)s, %(points)s, NOW(), NOW());"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def subtract_points(cls, user_id, points):
        query = "UPDATE users SET points = points - %(points)s, updated_at = NOW() WHERE user_id = %(user_id)s;"
        data = {"user_id": user_id, "points": points}
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def add_points(cls, user_id, points):
        query = "UPDATE users SET points = points + %(points)s, updated_at = NOW() WHERE user_id = %(user_id)s;"
        data = {"user_id": user_id, "points": points}
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def delete_user(cls, data):
        query  = "DELETE FROM users WHERE user_id = %(user_id)s;"
        return connectToMySQL(db).query_db(query,data)
