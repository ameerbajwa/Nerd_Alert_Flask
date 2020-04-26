from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class EnterUserQuizResults(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        quiz_iteration = SQL_queries_to_database.find_quiz_iteration(data['user_id'], data['quiz_id'])

        if SQL_queries_to_database.find_quiz_iteration(quiz_iteration['quiz_iteration']+1):
            return {'message': 'A quiz with that iteration already exists'}, 400

        if SQL_queries_to_database.find_user_quiz_results(data['user_id'], data['quiz_id'], quiz_iteration['quiz_iteration']+1):
            return {'message': 'User has already taken this quiz'}, 400

        committed = SQL_queries_to_database.implant_users_quiz_score(data, quiz_iteration['quiz_iteration'])

        if committed:
            return {'message': "Quiz created successfully."}, 201


class RetrieveUserQuizResults(Resource):

    # jwt_required
    def post(self):
        data = request.get_json()

        user_quiz_results = SQL_queries_to_database.find_user_quiz_results(data['user_id'], data['quiz_id'])
        restructured_user_quiz_results = {}
        for i in range(0, len(user_quiz_results)):
            restructured_user_quiz_results['Iteration: ' + user_quiz_results[i]['iteration']] = user_quiz_results[i]
        return jsonify(restructured_user_quiz_results)


class RetrieveNewQuizIteration(Resource):

    def post(self):
        data = request.get_json()

        quiz_iteration = SQL_queries_to_database.find_quiz_iteration(data['user_id'], data['quiz_id'])
        quiz_iteration['quiz_iteration'] += 1
        return jsonify(quiz_iteration)

