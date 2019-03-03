# pylint: disable=too-few-public-methods,no-self-use
from marshmallow.fields import UUID, Nested, String
from marshmallow_sqlalchemy import ModelSchema

from api.models import User
from api.models.base_model import session
from api.schemas.base_schema import BaseSchema


class UserSchema(ModelSchema, BaseSchema):
    id = UUID(required=False)

    class Meta:
        model = User
        strict = True
        sqla_session = session
        exclude = ("password",)
