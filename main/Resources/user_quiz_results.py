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