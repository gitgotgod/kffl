
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class UserPointsManager:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        username = username.strip()
        if username:
            new_user = {"id": len(self.users) + 1, "name": username, "points": 0}
            self.users.append(new_user)

    def get_users(self):
        return self.users

    def update_points(self, user_id, points):
        for user in self.users:
            if user["id"] == user_id:
                user["points"] += points
                break

    def subtract_points(self, user_id, points):
        for user in self.users:
            if user["id"] == user_id:
                user["points"] -= points
                break

    def delete_user(self, user_id):
        self.users = [user for user in self.users if user["id"] != user_id]