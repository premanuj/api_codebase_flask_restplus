class GenericException(Exception):
    def __init__(self, message="Generic Exception", detail=None):
        super(GenericException, self).__init__(self)

        self.message = message
        self.detail = detail

    def __dict__(self):
        return {"message": self.message, "error": self.detail}

    def __str__(self):
        return str({{"message": self.message, "error": self.detail}})

