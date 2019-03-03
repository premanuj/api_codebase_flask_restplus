from .generic_exception import GenericException


class DatabaseException(GenericException):
    def __init__(self, message="Databse Exception", detail=None):
        super(DatabaseException, self).__init__(self)

        self.message = message
        self.detail = detail
