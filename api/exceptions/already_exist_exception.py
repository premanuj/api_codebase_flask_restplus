from .generic_exception import GenericException


class AlreadyExistException(GenericException):
    def __init__(self, message="Data already exist", detail=None):
        super(AlreadyExistException, self).__init__(self)

        self.message = message
        self.detail = detail
