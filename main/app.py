from flask import Flask, jsonify
from flask_restful import Resource, Api

from connection import connect_to_mysql_database

app = Flask(__name__)
api = Api(app)

class Users(Resource):

    def get(self):
        connection_to_database = connect_to_mysql_database()

        cursor = connection_to_database.cursor()
        sql_query = "SELECT * FROM users"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        connection_to_database.close()

        users = []
        for result in results:
            users.append(result)

        return jsonify(users)


api.add_resource(Users, '/users')

app.run(port=6373, debug=True)
