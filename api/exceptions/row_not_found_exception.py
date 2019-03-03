from .generic_exception import GenericException


class RowNotFoundException(GenericException):
    def __init__(self, message="No row with the given identfier found", detail=None):
        super(RowNotFoundException, self).__init__(self)

        self.message = message
        self.detail = detail
