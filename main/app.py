from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from API_classes import users, security, quizzes, quiz_questions, user_quiz_results, user_question_results
import config

app = Flask(__name__)
api = Api(app)
app.secret_key = config.APP_SECRET_KEY
jwt = JWT(app, security.authenticate, security.identity)

api.add_resource(users.UserRegister, '/register_user', methods=['POST'])
api.add_resource(quizzes.Quizzes, '/quizzes', methods=['GET', 'POST'])
api.add_resource(quizzes.Quiz, '/quiz/<string:identifier>/<string:value>', methods=['GET'])
api.add_resource(quiz_questions.quizQuestions, '/quiz_questions', methods=['GET', 'POST'])
api.add_resource(user_quiz_results.userQuizResults, '/user_quiz_results', methods=['POST'])
api.add_resource(user_question_results.userQuestionResults, '/user_question_results', methods=['POST'])

app.run(port=6373, debug=True)
