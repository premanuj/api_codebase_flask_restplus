from typing import List
from sqlalchemy import inspect
from marshmallow import ValidationError
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow_sqlalchemy import ModelSchema


class BaseSchema:
    @classmethod
    def model_hybrid_columns(cls) -> List[str]:
        if not issubclass(cls, ModelSchema):
            raise Exception(
                'class "%s" is not subclass of "%s"' % (cls.__name__, ModelSchema.__name__)
            )

        return [
            attribute.__name__
            for attribute in inspect(cls.Meta.model).all_orm_descriptors
            if isinstance(attribute, hybrid_property)
        ]

    @classmethod
    def model_columns(cls) -> List[str]:
        if hasattr(cls, "Meta") and hasattr(cls.Meta, "selects"):
            return cls.Meta.selects

        if not issubclass(cls, ModelSchema):
            raise Exception(f"class {cls.__name__} is not subclass of {ModelSchema.__name__}")

        columns = [c.name for c in inspect(cls.Meta.model).columns]
        return columns

    @classmethod
    def model_relationships(cls) -> List[str]:
        if hasattr(cls, "Meta") and hasattr(cls.Meta, "joins"):
            return cls.Meta.joins

        if not issubclass(cls, ModelSchema):
            raise Exception(
                'class "%s" is not subclass of "%s"' % (cls.__name__, ModelSchema.__name__)
            )
        relationships = inspect(cls.Meta.model).relationships
        return [k for k, _ in relationships.items()]

    @classmethod
    def object_id_exists(cls, object_id, model):
        if not model.exists(object_id):
            raise ValidationError(f"Id {object_id} does not exists in {model.__table__name}")
