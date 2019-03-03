# pylint: disable=redefined-builtin
from marshmallow.exceptions import ValidationError

from api.exceptions import InvalidPayloadException, RowNotFoundException


class BaseService:
    model = None
    model_schema = None

    @classmethod
    def fetch(cls, params):
        return cls.model.fetch(params)

    @classmethod
    def fetch_single(cls, params):
        return cls.model.fetch_single(params)

    @classmethod
    def fetch_by_id(cls, id: str or int):
        data = cls.model.fetch_by_id(id)
        if not data:
            raise RowNotFoundException()

        return data

    @classmethod
    def create(cls, data: dict):
        try:
            schema = cls.model_schema(many=False)
            model_data, errors = schema.load(data)

            if errors:
                raise InvalidPayloadException("Invalid payload", errors)

            cls.model.create(model_data)

            return model_data

        except ValidationError as error:
            raise InvalidPayloadException("Invalid payload", detail=error.messages)

    @classmethod
    def update(cls, id, data: dict):
        try:
            old = cls.fetch_by_id(id)
            if not old:
                raise RowNotFoundException()
            data["id"] = id
            schema = cls.model_schema(many=False, partial=True)
            model_data, errors = schema.load(data)

            if errors:
                raise InvalidPayloadException("Invalid Payload", errors)

            cls.model.update(model_data)

            return model_data
        except ValidationError as error:
            raise InvalidPayloadException("Invalid payload", detail=error.messages)

    @classmethod
    def delete(cls, id: str or int):
        old = cls.fetch_by_id(id)
        if not old:
            raise RowNotFoundException()

        cls.model.delete(old)
