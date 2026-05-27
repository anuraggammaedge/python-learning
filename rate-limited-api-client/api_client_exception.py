# Base Exception
class APIClientError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Specific Exceptions
class APITimeoutError(APIClientError):
    pass


class RateLimitError(APIClientError):
    pass


class CircuitBreakerOpenError(APIClientError):
    pass


class APIRequestError(APIClientError):
    pass