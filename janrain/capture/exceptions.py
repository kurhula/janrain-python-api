""" Exceptions for the Janrain API library. """

class JanrainApiException(Exception):
    """ Base class for all Janrain API exceptions. """
    pass

class JanrainCredentialsError(Exception):
    """ Exception for credential errors (eg. Missing credentials) """
    pass

class JanrainConfigError(Exception):
    """ Exception for credential configuration file errors """
    def __init__(self, message=None, **kwargs):
        try:
            if message is None:
                message = "Could not find key '{}' in '{}'." \
                          .format(kwargs['key'], kwargs['file'])
        finally:
            super(JanrainConfigError, self).__init__(message)

class InvalidApiCallError(JanrainApiException):
    """ Request for a non-existing API call. """
    # DEPRECATED (bad API calls include an error in the JSON response)
    def __init__(self, api_call, status):
        message = "Invalid API call: {} ({})".format(api_call, status)
        JanrainApiException.__init__(self, message)

class JanrainInvalidUrlError(JanrainApiException):
    """ Invalid URL. """
    # DEPRECATED (bad application names include an error in the JSON response)
    pass

class ApiResponseError(JanrainApiException):
    """ An error response from the capture API. """
    def __init__(self, code, error, error_description, response):
        JanrainApiException.__init__(self, error_description)
        self.code = code
        self.error = error
        self.response = response
