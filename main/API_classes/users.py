from SQL_history.connection import connect_to_mysql_database
from SQL_history.users_table_SQL_statements import select_user_by_username, select_user_by_user_id

from flask_restful import Resource, request

import datetime


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
        connection_to_database = connect_to_mysql_database()
        cursor = connection_to_database.cursor()
        sql_query = select_user_by_username
        cursor.execute(sql_query, (username,))
        results = cursor.fetchone()
        connection_to_database.close()

        if results:
            user = cls(results['user_id'], results['username'], results['password'], results['email'], results['date_created'], results['last_login'])
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection_to_database = connect_to_mysql_database()
        cursor = connection_to_database.cursor()
        sql_query = select_user_by_user_id
        cursor.execute(sql_query, (_id,))
        results = cursor.fetchone()
        connection_to_database.close()

        if results:
            user = cls(*results)
        else:
            user = None
        return user


class UserRegister(Resource):

    def post(self):
        connection_to_database = connect_to_mysql_database()
        data = request.get_json()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400

        cursor = connection_to_database.cursor()
        query = "INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (data['id'], data['username'], data['password'], data['email'], str(datetime.datetime.now()), str(datetime.datetime.now())))

        connection_to_database.commit()
        connection_to_database.close()

        return {'message': "User created successfully."}, 201
