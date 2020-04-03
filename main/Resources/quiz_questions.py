from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class quizQuestions(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        committed_list = []
        for k in data.keys():
            committed = SQL_queries_to_database.create_quiz_question(data[k])
            committed_list.append(committed)

        if None in committed_list:
            return {'message': 'Quiz questions created successfully.'}, 201

    # @jwt_required()
    def get(self):
        data = request.get_json()

        quiz_questions = SQL_queries_to_database.find_quiz_questions(data['quiz_id'], data['user_id'])
        return jsonify(quiz_questions)
