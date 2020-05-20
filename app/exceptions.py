"""App Exceptions

Declaration of App Exceptions
"""
class Error(Exception):
    """Base class for exceptions in this module."""


class ValidationError(ValueError):
    """Validation Error for exceptions in this app."""


class ParameterExpected(Error):
    """Parameter Expected for exceptions in this app."""
    def __init__(self, message):
        super().__init__()
        #self.expression = expression
        self.message = message





# Http Api Errors
class RequestException(IOError):
    """Request Exception for exceptions in this app."""
    # def __init__(self, *args, **kwargs):
        # super(RequestException, self).__init__(*args, **kwargs)


class MongoServerError(Error):
    """Mongo Server for exceptions in this app."""
    def __init__(self, message):
        super().__init__()
        #self.expression = expression
        self.message = message


class MongoUnknownError(Error):
    """Mongo Unknown for exceptions in this app."""
    def __init__(self, message):
        super().__init__()
        #self.expression = expression
        self.message = message
