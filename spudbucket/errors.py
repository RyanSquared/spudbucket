class FormError(Exception):
    """
    Base error class for all form validation errors. This can be handled
    by default for all of Flask's requests, and all errors raised by a
    validator should extend off this class.
    """
    pass


class FormKeyError(FormError):
    """
    This error is raised if a validator is assigned to a page and the
    page has the methods configured for form data, but the form data
    does not exist.
    """

    def __init__(self, key, form):
        self.key = key
        self._form = form

    def __str__(self):
        return "Expected key %r for form %r" % (self.key, self._form)


class ValidationError(FormError):
    """
    This error is raised by `validator.raise_error()` if a validator does
    not find the data to fit the requirements. This could mean that the
    UI was not designed with the proper constraints or someone entered
    invalid data.
    """

    def __init__(self, key, value, validator, message=None, exception=None):
        self.key = key
        self.value = value
        self.message = message
        self.exception = exception
        self._validator = validator

    def __str__(self):
        post = ""
        if self.message is not None:
            post += " (%r)" % self.message
        if self.exception is not None:
            post += " <%r>" % self.exception
        return "%r: %r failed test for %r%s" % (
            self.key, self.value, self._validator, post)


class InvalidSessionError(FormError):
    """
    This could be useful for if a session times out in the middle of
    something. An error handler could be caught and automatically redirect
    users to a login page if an invalid session is detected. This is an
    empty container error with no functionality.
    """

    def __str__(self):
        return "Invalid or missing Flask session for request"
