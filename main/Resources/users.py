from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class User:
    def __init__(self, _id, username, password, email, date_created, last_login):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email
        self.date_created = date_created
        self.last_login = last_login

    @classmethod
    def find_by_username(cls, username):
        results = SQL_queries_to_database.find_user_by_username(username)

        if results:
            user = cls(results['user_id'], results['username'], results['password'], results['email'],
                       results['date_created'], results['last_login'])
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id):
        results = SQL_queries_to_database.find_user_by_id(_id)

        if results:
            user = cls(*results)
        else:
            user = None
        return user


class UserRegister(Resource):

    def post(self):
        data = request.get_json()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400

        user_id = SQL_queries_to_database.find_user_id()
        committed = SQL_queries_to_database.create_user(data, user_id['user_id'])

        if committed:
            return {'message': "User created successfully."}, 201


class UserInfo(Resource):

    def get(self):
        data = request.get_json()

        user = SQL_queries_to_database.find_user_by_username(data['username'])

        return jsonify(user)
