from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask_jwt_extended.exceptions import NoAuthorizationError
from errors import UnauthorizedError, InternalServerError

class LandingPage(Resource):

    @jwt_required
    def get(self):
        try:
            user_id = get_jwt_identity()
            return {
                'message': 'You are welcome',
                'code': str(user_id)
                }, 200
        except NoAuthorizationError as e:
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
        