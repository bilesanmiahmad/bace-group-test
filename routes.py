from auth import Signup, LoginApi
from landingpage import LandingPage


def initialize_routes(api):
    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(LandingPage, '/api/dashboard')
