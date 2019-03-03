from .generic_exception import GenericException


class InvalidPayloadException(GenericException):
    def __init__(self, message="Invalid Payload Exception", detail=None):
        super(InvalidPayloadException, self).__init__(self)

        self.message = message
        self.detail = detail

