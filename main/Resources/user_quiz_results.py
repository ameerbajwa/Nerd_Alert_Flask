from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class EnterUserQuizResults(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        if SQL_queries_to_database.find_user_quiz_result(data['user_id'], data['quiz_id'], data['quiz_iteration']):
            return {'message': 'User has already taken this quiz'}, 400

        committed = SQL_queries_to_database.implant_users_quiz_score(data)

        if committed:
            return {'message': "Quiz results entered successfully."}, 201


class RetrieveUserQuizResults(Resource):

    # jwt_required
    def post(self):
        data = request.get_json()

        user_quiz_results = SQL_queries_to_database.find_user_quiz_results(data['user_id'], data['quiz_id'])
        restructured_user_quiz_results = {}
        for i in range(0, len(user_quiz_results)):
            restructured_user_quiz_results['Iteration: ' + str(user_quiz_results[i]['iteration'])] = user_quiz_results[i]
        return jsonify(restructured_user_quiz_results)


class RetrieveUserQuizResult(Resource):

    # jwt_required
    def get(self, user_id, quiz_id, quiz_iteration):
        user_quiz_result = SQL_queries_to_database.find_user_quiz_result(user_id, quiz_id, quiz_iteration)
        return jsonify(user_quiz_result)


class RetrieveNewQuizIteration(Resource):

    def post(self):
        data = request.get_json()

        quiz_iteration = SQL_queries_to_database.find_quiz_iteration(data['user_id'], data['quiz_id'])
        quiz_iteration['iteration'] += 1
        return jsonify(quiz_iteration)

