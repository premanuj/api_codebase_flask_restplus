from .generic_exception import GenericException


class ConstraintException(GenericException):
    def __init__(self, message="Detail Constrain Voilation Exception", detail=None):
        super(ConstraintException, self).__init__(self)

        self.message = message
        self.detail = detail
