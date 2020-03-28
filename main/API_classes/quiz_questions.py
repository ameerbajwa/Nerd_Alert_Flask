from flask_restful import Resource, request

from SQL_history import SQL_queries_to_database


class quizQuestions(Resource):

    @staticmethod
    def post():
        data = request.get_json()
        print(data)

        committed_list = []
        for d in data:
            committed = SQL_queries_to_database.insert_quiz_question(d)
            committed_list.append(committed)

        if len(committed_list) < 10 or None in committed_list:
            return {'message': 'Quiz questions created successfully.'}, 201