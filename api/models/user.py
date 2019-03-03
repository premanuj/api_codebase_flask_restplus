# pylint: disable=too-few-public-methods,redefined-builtin
import passlib
from uuid import uuid4, UUID
from api.models.meta import Base
from api.models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy_utils import UUIDType, EmailType, PasswordType


class User(Base, BaseModel):
    __tablename__ = "users"

    id = Column(UUIDType(binary=False), primary_key=True)
    email = Column(EmailType, unique=True)
    password = Column(String)

    def __init__(self, *, id: UUID = None, email: str, password: str):
        if not id:
            id = uuid4()
        self.id = id
        self.email = email
        self.password = password
