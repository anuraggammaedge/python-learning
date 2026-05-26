class ConnectionFailedError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class QueryTimeoutError(Exception):
    def __init__(self, message, timeout=5):
        self.message = message
        self.timeout = timeout
        super().__init__(self.message)

class MaxRetriesExceededError(Exception):
    def __init__(self, retries):
        self.retries = retries
        super().__init__(
            f"Maximum retry limit exceeded: {self.retries}"
        )