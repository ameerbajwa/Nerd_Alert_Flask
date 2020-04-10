from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class GenerateQuizQuestions(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        committed_list = []
        for k in data.keys():
            committed = SQL_queries_to_database.create_quiz_question(data[k])
            committed_list.append(committed)

        if None in committed_list:
            return {'message': 'Quiz questions created successfully.'}, 201


class RetrieveQuizQuestions(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        quiz_questions = SQL_queries_to_database.find_quiz_questions(data['quiz_id'], data['user_id'])
        return jsonify(quiz_questions)

    # # @jwt_required()
    # def delete(self):
    #     data = request.get_json()
    #
    #     executed = SQL_queries_to_database.delete_quiz_question(data['question_id'])
    #     if executed:
    #         return {'message': 'Quiz question {} has been deleted'.format(data['question'])}
