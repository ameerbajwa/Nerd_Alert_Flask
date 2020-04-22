from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class EnterUserQuestionResults(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        if SQL_queries_to_database.find_user_question_results(data['quiz_id'], data['user_id']):
            return {'message': 'User has already answered this question'}, 400

        committed_list = []
        for k in data.keys():
            committed = SQL_queries_to_database.implant_users_question_answers(data[k])
            committed_list.append(committed)

        if None in committed_list:
            return {'message': 'User questions results implanted successfully.'}, 201


class RetrieveUserQuestionResults(Resource):

    #jwt_required()
    def post(self):
        data = request.get_json()

        user_question_results = SQL_queries_to_database.find_user_question_results(data['quiz_id'], data['user_id'],
                                                                                   data['iteration'])
        restructured_user_question_results = {}
        for i in range(0, len(user_question_results)):
            restructured_user_question_results[i] = user_question_results[i]
        return jsonify(restructured_user_question_results)
