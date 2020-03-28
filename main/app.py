from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from API_classes import users, security, quizzes, quiz_questions
import config

app = Flask(__name__)
api = Api(app)
app.secret_key = config.APP_SECRET_KEY
jwt = JWT(app, security.authenticate, security.identity)

api.add_resource(users.UserRegister, '/register_user')
api.add_resource(quizzes.Quizzes, '/quizzes')
# api.add_resource(quizzes.Quiz, '/quiz/<string:identifier>/<string:value>')
# api.add_resource(quiz_questions.quizQuestions, '/quiz_questions')

app.run(port=6373, debug=True)
