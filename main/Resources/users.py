from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class User:
    def __init__(self, _id, username, password, email, date_created, last_login, admin, creator):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email
        self.date_created = date_created
        self.last_login = last_login
        self.admin = admin
        self.creator = creator

    @classmethod
    def find_by_username(cls, username):
        results = SQL_queries_to_database.find_user_by_username(username)

        if results:
            user = cls(results['user_id'], results['username'], results['password'], results['email'],
                       results['date_created'], results['last_login'], results['admin'], results['creator'])
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

    @classmethod
    def find_by_email(cls, _email):
        results = SQL_queries_to_database.find_user_by_email(_email)

        if results:
            user = cls(*results)
        else:
            user = None
        return user


class UserRegister(Resource):

    def post(self):
        data = request.get_json()

        if User.find_by_username(data['username']):
            return {'username error': 'A user with that username already exists'}, 400
        elif User.find_by_email(data['email']):
            return {'email error': 'A user with that email already exists'}, 400
        else:
            user_id = SQL_queries_to_database.find_user_id()
            committed = SQL_queries_to_database.create_user(data, user_id['user_id'])

            if committed:
                return {'message': "User created successfully."}, 201


class UserInfo(Resource):

    def get(self, username):

        user = SQL_queries_to_database.find_user_by_username(username)

        return jsonify(user)


class UserForgottenInfo(Resource):

    def get(self, email):

        user_info = SQL_queries_to_database.find_user_by_email(email)

        return user_info
