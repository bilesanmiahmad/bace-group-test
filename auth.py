from flask import request, Response
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
from flask_cors import cross_origin
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

class Signup(Resource):
    @cross_origin()
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            return {'email': user.email, 'id': str(user.id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class LoginApi(Resource):
    @cross_origin()
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Email or password invalid'}, 400
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
