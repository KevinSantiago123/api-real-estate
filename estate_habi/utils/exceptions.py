__author__ = 'kcastanedat'

@classmethod
class ExceptionPersonalized(Exception):
    """API exceptions, in case an exception is not sent,
    the class responds with an error by default."""

    def __init__(self, errors):
        self.errors = errors
        self.message = "An error has occurred"
        super().__init__(self.message)

    def __str__(self):
        return str(self.errors)
