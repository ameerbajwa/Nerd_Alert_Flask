from flask import Flask
from flask_restful import Api
from flask_mail import Mail, Message
from flask_jwt import JWT

from Resources import users, security, quiz, quiz_questions, user_quiz_results, user_question_results
import config
from customJSONEncoder import CustomJSONEncoder

app = Flask(__name__)
api = Api(app)
app.secret_key = config.APP_SECRET_KEY
app.json_encoder = CustomJSONEncoder

jwt = JWT(app, security.authenticate, security.identity)

mail_settings = {
    "MAIL_SERVER": 'ameerbajwa@gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'ameerbajwa',
    "MAIL_PASSWORD": 'hallo'
}

app.config.update(mail_settings)
mail = Mail(app)

api.add_resource(users.UserRegister, '/register_user', methods=['POST'])
api.add_resource(users.UserInfo, '/user_info/<string:username>', methods=['GET'])
api.add_resource(users.UserForgottenInfo, '/user_forgotten_info/<string:email>', methods=['GET'])

api.add_resource(quiz.GenerateQuiz, '/generate_quiz', methods=['POST'])
api.add_resource(quiz.RetrieveQuiz, '/retrieve_quiz', methods=['POST'])
api.add_resource(quiz.FindQuiz, '/find_quiz/<string:quiz_id>', methods=['GET'])
api.add_resource(quiz.UpdateQuiz, '/update_quiz/<string:quiz_id>', methods=['PUT'])
api.add_resource(quiz.DeleteQuiz, '/delete_quiz/<string:quiz_id>', methods=['PUT'])

api.add_resource(quiz_questions.GenerateQuizQuestions, '/generate_quiz_questions', methods=['POST'])
api.add_resource(quiz_questions.RetrieveQuizQuestions,
                 '/retrieve_quiz_questions/quizId/<string:quiz_id>/userId/<string:user_id>/<string:quiz_action>',
                 methods=['GET'])
api.add_resource(quiz_questions.RetrieveQuizQuestion,
                 '/retrieve_quiz_question/questionId/<string:question_id>', methods=['GET'])
api.add_resource(quiz_questions.UpdateQuizQuestion,
                 '/update_quiz_question/questionId/<string:question_id>', methods=['PUT'])
api.add_resource(quiz_questions.RetrieveQuizQuestionsByIds, '/retrieve_quiz_questions_by_ids', methods=['POST'])
api.add_resource(quiz_questions.RetrieveNumberOfQuizQuestions,
                 '/retrieve_number_of_quiz_questions/quizId/<string:quiz_id>', methods=['GET'])
# api.add_resource(quiz_questions.DeleteQuizQuestion, '/delete_quiz_question/<string:question_id>', methods=['DELETE'])

api.add_resource(user_quiz_results.EnterUserQuizResults, '/enter_user_quiz_results', methods=['POST'])
api.add_resource(user_quiz_results.RetrieveUserQuizResults, '/retrieve_user_quiz_results', methods=['POST'])
api.add_resource(user_quiz_results.RetrieveUserQuizResult,
                 '/retrieve_user_quiz_result/user_id/<string:userId>/quiz_id/<string:quizId>/quiz_iteration/<string:quizIteration>',
                 methods=['GET'])
api.add_resource(user_quiz_results.RetrieveNewQuizIteration, '/retrieve_quiz_iteration', methods=['POST'])

api.add_resource(user_question_results.EnterUserQuestionResults, '/enter_user_question_results', methods=['POST'])
api.add_resource(user_question_results.RetrieveUserQuestionResults, '/retrieve_user_question_results', methods=['POST'])

if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["ameerbajwa@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)

app.run(port=6373, debug=True)
