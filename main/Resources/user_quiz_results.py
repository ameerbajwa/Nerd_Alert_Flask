from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class EnterUserQuizResults(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        if SQL_queries_to_database.find_user_id_quiz_id(data['user_id'], data['quiz_id']):
            return {'message': 'User has already taken this quiz'}, 400

        committed = SQL_queries_to_database.implant_users_quiz_score(data)

        if committed:
            return {'message': "Quiz created successfully."}, 201


class RetrieveUserQuizResults(Resource):

    # jwt_required
    def post(self):
        data = request.get_json()

        user_quiz_results = SQL_queries_to_database.find_user_quiz_results(data['quiz_id'], data['user_id'])
        restructured_user_quiz_results = {}
        for i in range(0, len(user_quiz_results)):
            restructured_user_quiz_results['Iteration: ' + user_quiz_results[i]['iteration']] = user_quiz_results[i]
        return jsonify(restructured_user_quiz_results)