from flask_restful import Resource, request

from SQL_history import SQL_queries_to_database

class Quizzes(Resource):

    @staticmethod
    def get():
        quizzes = SQL_queries_to_database.select_all_quizzes()
        return quizzes


class Quiz(Resource):

    @staticmethod
    def get(identifier):
        if identifier.key() == 'username':
            quizzes = SQL_queries_to_database.find_quiz_by_username(identifier.value())
        elif identifier.key() == 'createdBy':
            quizzes = SQL_queries_to_database.find_quiz_by_creator(identifier.value())
        else:
            quizzes = SQL_queries_to_database.find_quiz_by_type(identifier.value())

        return quizzes

