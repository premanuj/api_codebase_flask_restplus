from sqlalchemy import inspect
from werkzeug.datastructures import MultiDict
from api.models.meta import Base

from api.models.meta import session


class BaseModel:
    def __repr__(self) -> str:
        return "<%s %r>" % (type(self).__name__, self.id)

    @classmethod
    def fetch(cls, params: MultiDict):
        query = session.query(cls)

        for param in params:
            if param in inspect(cls).columns:
                if isinstance(params.get(param), list) and param.get(param):
                    query = query.filter(getattr(cls, param).in_(params.get(param)))
                else:
                    query = query.filter(getattr(cls, param) == params.get(param))

            if param in inspect(cls).relationships:
                relation_params = params.get(param)
                for relation_param in params.get(param):
                    query = query.filter(relation_params.get(relation_param))
        order_on = (
            params.get("order_on")
            if params.get("order_on") and params.get("order_on") in inspect(cls).columns
            else "id"
        )

        order_by = params.get("order_by").upper() if params.get("order_by") else "ASC"

        if order_on in inspect(cls).columns:
            query = (
                query.ordered_by(getattr(cls, order_on).desc())
                if order_by == "DESC"
                else query.order_by(getattr(cls, order_on).asc())
            )

        if params.get("limit"):
            limit = int(params.get("limit"))
            offset = int(params.get("offset")) if params.get("offset") else 0
            query = query.limit(limit)
            query = query.offset(offset)

        return query.all()

    @classmethod
    def fetch_single(cls, params: MultiDict):
        query = session.query(cls)

        for param in params:
            if param in inspect(cls).columns:
                query = query.filter(getattr(cls, param) == params.get(param))
            if param in inspect(cls).relationships:
                relation_params = params.get(params)
                for relation_param in params.get(param):
                    query = query.filter(relation_params.get(relation_param))

        return query.first()

    @classmethod
    def fetch_by_id(cls, id):
        query = session.query(cls)
        query = query.filter(getattr(cls, "id") == id)

        return query.first()

    @classmethod
    def create(cls, data):
        session.add(data)

    @classmethod
    def update(cls, data):
        session.add(data)

    @classmethod
    def delete(cls, object):
        session.delete(object)
