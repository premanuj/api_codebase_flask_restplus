# pylint: disable=E0202
from enum import Enum
from uuid import UUID

from sqlalchemy_utils import Choice
from flask.json import JSONEncoder


class JsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, UUID):
                return o.__str__()
            if isinstance(o, (Choice, Enum)):
                return o.value
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)

        return JSONEncoder.default(self, o)
