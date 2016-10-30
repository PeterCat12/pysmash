class ExceptionWithStatusCode(Exception):
    def __init__(self, message, status_code):

        # Call the base class constructor with the parameters it needs
        super(ExceptionWithStatusCode, self).__init__(message)
        self.status_code = status_code


class ValidationError(ExceptionWithStatusCode):
    def __init__(self, message, status_code=400):
        super(ValidationError, self).__init__(message, status_code=status_code)


class ResponseError(ExceptionWithStatusCode):
    def __init__(self, message, status_code):
        super(ResponseError, self).__init__(message=message, status_code=status_code)
