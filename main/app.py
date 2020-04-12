from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Resources import users, security, quiz, quiz_questions, user_quiz_results, user_question_results
import config
from customJSONEncoder import CustomJSONEncoder

app = Flask(__name__)
api = Api(app)
app.secret_key = config.APP_SECRET_KEY
app.json_encoder = CustomJSONEncoder

jwt = JWT(app, security.authenticate, security.identity)

api.add_resource(users.UserRegister, '/register_user', methods=['POST'])
api.add_resource(users.UserInfo, '/user_info/<string:username>', methods=['GET'])

api.add_resource(quiz.GenerateQuiz, '/generate_quiz', methods=['POST'])
api.add_resource(quiz.RetrieveQuiz, '/retrieve_quiz', methods=['POST'])

api.add_resource(quiz_questions.GenerateQuizQuestions, '/generate_quiz_questions', methods=['POST'])
api.add_resource(quiz_questions.RetrieveQuizQuestions, '/retrieve_quiz_questions', methods=['POST'])

api.add_resource(user_quiz_results.EnterUserQuizResults, '/enter_user_quiz_results', methods=['POST'])
api.add_resource(user_question_results.EnterUserQuestionResults, '/enter_user_question_results', methods=['POST'])

app.run(port=6373, debug=True)
