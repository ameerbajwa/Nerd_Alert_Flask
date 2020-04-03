from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class Quiz(Resource):

    # @jwt_required()
    def get(self):
        data = request.get_json()
        results = {}

        if data['quiz_name'] is not None:
            quizzes = SQL_queries_to_database.find_quiz_by_name(data["quiz_name"])
        elif data['createdBy'] is not None:
            quizzes = SQL_queries_to_database.find_quiz_by_creator(data["createdBy"])
        elif data['source'] is not None:
            quizzes = SQL_queries_to_database.find_quiz_by_type(data["source"])
        else:
            quizzes = SQL_queries_to_database.find_all_quizzes()

        return jsonify(quizzes)

    # @jwt_required()
    def post(self):
        data = request.get_json()

        quiz_id = SQL_queries_to_database.find_new_quiz_id()

        if SQL_queries_to_database.find_quiz_by_id(quiz_id):
            return {'message': 'A quiz with that id already exists'}, 400

        committed = SQL_queries_to_database.create_quiz(data, quiz_id)

        if committed:
            return {'message': "Quiz created successfully."}, 201

