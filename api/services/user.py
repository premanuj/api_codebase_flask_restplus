from api.models import User
from api.schemas import UserSchema
from api.services.base_service import BaseService
from api.exceptions import AlreadyExistException


class UserService(BaseService):
    model = User
    model_schema = UserSchema

    @classmethod
    def register(cls, data):
        email = data.get("email")
        old_user = super(UserService, cls).fetch_single({"email": email})
        old_user = cls.model_schema().dump(old_user).data
        if old_user:
            raise AlreadyExistException(f'User with email "{email}" already exists')

        user = super(UserService, cls).create(data)
        data = cls.model_schema().dump(user).data
        return user
