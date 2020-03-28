from flask_restful import Resource, request
from flask_jwt import jwt_required

from SQL_history import SQL_queries_to_database


class Quizzes(Resource):

    @staticmethod
    @jwt_required
    def get():
        quizzes = SQL_queries_to_database.select_all_quizzes()
        return quizzes

    @staticmethod
    @jwt_required
    def post():
        data = request.get_json()
        print(data)

        # if SQL_queries_to_database.find_quiz_by_id(data['quiz_id']):
        #     return {'message': 'A quiz '}, 400

        committed = SQL_queries_to_database.insert_quiz(data)

        if committed:
            return {'message': "Quiz created successfully."}, 201


class Quiz(Resource):

    @staticmethod
    @jwt_required
    def get(identifier, value):
        if identifier == 'username':
            quizzes = SQL_queries_to_database.find_quiz_by_username(value)
        elif identifier == 'createdBy':
            quizzes = SQL_queries_to_database.find_quiz_by_creator(value)
        else:
            quizzes = SQL_queries_to_database.find_quiz_by_type(value)

        return quizzes


