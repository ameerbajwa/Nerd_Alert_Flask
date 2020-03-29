from flask_restful import Resource, request
from flask_jwt import jwt_required

from SQL_history import SQL_queries_to_database


class quizQuestions(Resource):

    @jwt_required()
    def post(self):
        data = request.get_json()

        committed_list = []
        for k in data.keys():
            print(k)
            print(data[k])
            committed = SQL_queries_to_database.create_quiz_question(data[k])
            committed_list.append(committed)

        if None in committed_list:
            return {'message': 'Quiz questions created successfully.'}, 201