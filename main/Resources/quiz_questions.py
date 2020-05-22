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

        if len(quiz_questions) == 0:
            return {'Completed the quiz': 'You have completed all the questions to this quiz!'}, 200
        elif len(quiz_questions) < 10:
            return {'Quiz Creator?':
                        'Quiz creator needs to finish adding more questions to make a complete 10 question quiz'}
        else:
            restructured_quiz_questions = {}
            for i in range(0, len(quiz_questions)):
                restructured_quiz_questions[str(i + 1)] = quiz_questions[i]
            return jsonify(restructured_quiz_questions)


class RetrieveQuizQuestion(Resource):

    # @jwt_required()
    def get(self, question_id):
        quiz_question = SQL_queries_to_database.find_quiz_question(question_id)

        return jsonify(quiz_question)


class RetrieveQuizQuestionsByIds(Resource):

    # @jwt_required
    def post(self):
        data = request.get_json()

        quiz_questions = SQL_queries_to_database.find_quiz_questions_by_ids(data['question_ids'])

        restructured_quiz_questions = {}
        for i in range(0, len(quiz_questions)):
            restructured_quiz_questions[quiz_questions[i]['question_id']] = quiz_questions[i]
        return jsonify(restructured_quiz_questions)


class RetrieveNumberOfQuizQuestions(Resource):

    # jwt_required()
    def get(self, quiz_id):

        number_of_questions = SQL_queries_to_database.find_number_of_quiz_questions(quiz_id)

        return {'number of questions in quiz': number_of_questions[0]['COUNT(*)']}, 200

    # # @jwt_required()
    # def delete(self):
    #     data = request.get_json()
    #
    #     executed = SQL_queries_to_database.delete_quiz_question(data['question_id'])
    #     if executed:
    #         return {'message': 'Quiz question {} has been deleted'.format(data['question'])}
