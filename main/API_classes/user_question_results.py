from flask_restful import Resource, request
from flask_jwt import jwt_required

from SQL_history import SQL_queries_to_database


class userQuestionResults(Resource):

    @jwt_required()
    def post(self):
        data = request.get_json()

        if SQL_queries_to_database.find_user_id_question_id(data['quiz_id'], data['user_id']):
            return {'message': 'User has already answered this question'}, 400

        committed_list = []
        for k in data.keys():
            committed = SQL_queries_to_database.implant_users_question_answers(data[k])
            committed_list.append(committed)

        if None in committed_list:
            return {'message': 'User questions results implanted successfully.'}, 201
