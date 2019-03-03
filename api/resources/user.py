from typing import List
from flask import request
from flask_restplus import Resource, fields, reqparse

from api.resources.api import api as user_api
from api.utils.common import json_response
from api.services.meta_service import MetaService
from api.utils.database import session_commit_context
from api.services import UserService
from api.services.api_service import ApiResource
from api.schemas import UserSchema
from api.models import User

meta = MetaService(UserSchema)

resource = ApiResource(user_api, meta)


@user_api.route("/users")
class UserList(Resource):
    @resource.index
    def get(self) -> List[User]:
        return UserService.fetch(request.args)


@user_api.route("/registration")
class UserRegistration(Resource):
    def post(self):
        with session_commit_context():
            result = UserService.register(user_api.payload)
            return result


@user_api.route("/login")
class UserLogin(Resource):
    @resource.post
    def post(self):
        return


@user_api.route("/logout/access")
class UserLogoutAccess(Resource):
    def post(self):
        return {"message": "User logout"}


@user_api.route("/logout/refresh")
class UserLogoutRefresh(Resource):
    def post(self):
        return {"message": "User logout"}


@user_api.route("/token/refresh")
class TokenRefresh(Resource):
    def post(self):
        return {"message": "Token refresh"}


# class AllUsers(Resource):
#     def get(self):
#         return {"message": "List of users"}

#     def delete(self):
#         return {"message": "Delete all users"}


@user_api.route("/secret")
class SecretResource(Resource):
    def get(self):
        return {"answer": 42}

