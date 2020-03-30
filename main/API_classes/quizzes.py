from flask_restful import Resource, request
from flask_jwt import jwt_required

from SQL_history import SQL_queries_to_database


class Quizzes(Resource):

    @jwt_required()
    def get(self):
        quizzes = SQL_queries_to_database.select_all_quizzes()
        return quizzes

    @jwt_required()
    def post(self):
        data = request.get_json()

        if SQL_queries_to_database.find_quiz_by_id(data['quiz_id']):
            return {'message': 'A quiz with that id already exists'}, 400

        quiz_id = SQL_queries_to_database.find_new_quiz_id()
        committed = SQL_queries_to_database.create_quiz(data, quiz_id)

        if committed:
            return {'message': "Quiz created successfully."}, 201


class Quiz(Resource):

    @jwt_required()
    def get(self, identifier, value):
        if identifier == 'username':
            quizzes = SQL_queries_to_database.find_quiz_by_username(value)
        elif identifier == 'createdBy':
            quizzes = SQL_queries_to_database.find_quiz_by_creator(value)
        else:
            quizzes = SQL_queries_to_database.find_quiz_by_type(value)

        return quizzes


