from http import HTTPStatus
from flask_restplus import Api
from marshmallow.exceptions import ValidationError
from api.utils.common import log_error, error_response
from api import resources


api = Api(
    version="1.0",
    title="API-V1",
    description="API using flask restplus",
    prefix="/api/v1",
    # authorizations=authorizations,
)

# api.add_resource(resources.UserRegistration, "/registration")
# api.add_resource(resources.UserLogin, "/login")
# api.add_resource(resources.UserLogoutAccess, "/logout/access")
# api.add_resource(resources.UserLogoutRefresh, "/logout/refresh")
# api.add_resource(resources.TokenRefresh, "/token/refresh")
# api.add_resource(resources.UserList, "/users")
# api.add_resource(resources.SecretResource, "/secret")


@api.errorhandler
def exception(error):
    log_error(error.message, HTTPStatus.NOT_ACCEPTABLE)
    return error_response(error.message, HTTPStatus.INTERNAL_SERVER_ERROR)
