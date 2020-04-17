from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class GenerateQuiz(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        quiz_id = SQL_queries_to_database.find_new_quiz_id()

        if SQL_queries_to_database.find_quiz_by_id(quiz_id['quiz_id']+1):
            return {'message': 'A quiz with that id already exists'}, 400

        committed = SQL_queries_to_database.create_quiz(data, quiz_id['quiz_id'])

        if committed:
            return {'message': "Quiz created successfully."}, 201


class RetrieveQuiz(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        if data['quiz_name'] is not None:
            quizzes = SQL_queries_to_database.find_quiz_by_name(data["quiz_name"], data['user_id'], data['users_quizzes'])
        elif data['createdBy'] is not None:
            quizzes = SQL_queries_to_database.find_quiz_by_creator(data["createdBy"], data['user_id'], data['users_quizzes'])
        elif data['source'] is not None:
            quizzes = SQL_queries_to_database.find_quiz_by_type(data["source"], data['user_id'], data['users_quizzes'])
        else:
            quizzes = SQL_queries_to_database.find_all_quizzes(data['user_id'], data['users_quizzes'])

        if len(quizzes) == 1:
            return jsonify(quizzes)
        else:
            restructured_quizzes = {}
            for i in range(0,len(quizzes)):
                restructured_quizzes[str(i+1)] = quizzes[i]
            return jsonify(restructured_quizzes)
