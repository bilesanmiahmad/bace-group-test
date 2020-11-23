from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS, cross_origin
from routes import initialize_routes
from database.db import initialize_db
from errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/bace-db'
}

initialize_db(app)
initialize_routes(api)

app.run()