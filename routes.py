from auth import Signup, LoginApi


def initialize_routes(api):
    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
