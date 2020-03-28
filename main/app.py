from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from API_classes import users, security
import config

app = Flask(__name__)
api = Api(app)
app.secret_key = config.APP_SECRET_KEY
jwt = JWT(app, security.authenticate, security.identity)

api.add_resource(users.UserRegister, '/register_user')

app.run(port=6373, debug=True)
