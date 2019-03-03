from .generic_exception import GenericException


class FileOperationException(GenericException):
    def __init__(self, message="File operation exceprion", detail=None):
        super(FileOperationException, self).__init__(self)

        self.message = message
        self.detail = detail
