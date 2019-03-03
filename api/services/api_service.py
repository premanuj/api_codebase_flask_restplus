from http import HTTPStatus
from typing import Callable, Union
from flask_restplus import Api as BaseApi, Namespace
from api.services.meta_service import MetaService
from api.decorators.marshmallow_with import marshmallow_with

# from api.services.meta_service import
Api = Union[BaseApi, Namespace]


class ApiResource:
    def __init__(self, api: Api, meta):
        self.api = api
        self.meta = meta
        self.model = api.add_model(meta.api_model.name, meta.api_model)

    def index(self, function: Callable) -> Callable:
        mm_with = marshmallow_with(
            self.meta.schema_class, many=True, strict=True, request_parser=self.meta.index_parser
        )
        expect = self.api.expect(self.meta.index_parser)
        doc = self.api.doc(model=[self.model])

        return mm_with(expect(doc(function)))

    def get(self, function: Callable) -> Callable:
        expect = self.api.expect(self.meta.view_parser)
        doc = self.api.doc(model=self.model)
        mm_with = marshmallow_with(
            self.meta.schema_class, many=False, strict=True, request_parser=self.meta.view_parser
        )

        return expect(doc(mm_with(function)))

    def post(self, function: Callable) -> Callable:
        response_status = HTTPStatus.CREATED
        mm_with = marshmallow_with(
            self.meta.schema_class, many=False, strict=True, response_status=response_status
        )
        expect = self.api.expect(self.model)
        response = self.api.response(response_status, response_status.phrase, model=self.model)

        return response(mm_with(expect(function)))

    def put(self, function: Callable) -> Callable:
        # @validate_schema(put_validator)
        doc = self.api.doc(model=self.model)
        expect = self.api.expect(self.model)
        mm_with = marshmallow_with(self.meta.schema_class, many=False, strict=True)

        return doc(mm_with(expect(function)))

    def patch(self, function: Callable) -> Callable:
        doc = self.api.doc(model=self.model)
        expect = self.api.expect(self.model)
        mm_with = marshmallow_with(self.meta.schema_class, many=False, strict=True)

        return doc(mm_with(expect(function)))

    def delete(self, function: Callable) -> Callable:
        response_status = HTTPStatus.NO_CONTENT
        response = self.api.response(response_status, response_status.phrase)

        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            return None, response_status

        return response(wrapper)
