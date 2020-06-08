from flask import jsonify
from flask_restful import Resource, request
from flask_jwt import jwt_required

from Models import SQL_queries_to_database


class GenerateQuizQuestions(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_json()

        id = SQL_queries_to_database.create_quiz_question(data)

        return {'question_id': id}, 200


class RetrieveQuizQuestions(Resource):

    # @jwt_required()
    def get(self, quiz_id, user_id, quiz_action):

        quiz_questions = SQL_queries_to_database.find_quiz_questions(quiz_id, user_id, quiz_action)

        if quiz_action == "Taking_Quiz":
            if len(quiz_questions) == 0:
                return {'Completed the quiz': 'You have completed all the questions to this quiz!'}, 200
            elif len(quiz_questions) < 10:
                return {'Quiz Creator?':
                            'Quiz creator needs to finish adding more questions to make a complete 10 question quiz'}
            else:
                restructured_quiz_questions = {}
                for i in range(0, len(quiz_questions)):
                    restructured_quiz_questions[i + 1] = quiz_questions[i]
                return jsonify(restructured_quiz_questions)
        elif quiz_action == "Editing_Questions":
            if len(quiz_questions) == 0:
                return {'No questions': 0}
            else:
                restructured_quiz_questions = {}
                for i in range(0, len(quiz_questions)):
                    restructured_quiz_questions[i + 1] = quiz_questions[i]
                return jsonify(restructured_quiz_questions)


class RetrieveQuizQuestion(Resource):

    # @jwt_required()
    def get(self, question_id):
        quiz_question = SQL_queries_to_database.find_quiz_question(question_id)

        return jsonify(quiz_question)


class UpdateQuizQuestion(Resource):

    # @jwt_required()
    def put(self, question_id):
        data = request.get_json()

        committed = SQL_queries_to_database.revise_quiz_question(data, question_id)

        if committed:
            return {'message': 'quiz question was updated successfully'}

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
