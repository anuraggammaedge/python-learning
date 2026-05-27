import datetime
import requests
import re
import time
import functools
from api_client_exception import APIClientError, APIRequestError, APITimeoutError, CircuitBreakerOpenError, RateLimitError

def retry_with_backoff(max_retries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt <= max_retries:
                try:
                    return func(*args, **kwargs)
                
                except (APITimeoutError, APIRequestError, APIClientError) as e:
                    if attempt == max_retries:
                        raise

                    delay = 2 ** attempt

                    print(
                        f"Retry attempt {attempt + 1} "
                        f"after {delay}s due to error: {e}"
                    )

                    time.sleep(delay)

                    attempt += 1

                except CircuitBreakerOpenError:
                    raise
                except RateLimitError:
                    raise
        return wrapper
    return decorator


class ApiClient:

    API_URL_REGEX = re.compile(
        r"^https?:\/\/"             # http:// or https://
        r"([\w\-]+\.)+[\w\-]+"      # domain
        r"(:\d{1,5})?"              # optional port
        r"(\/.*)?$"                 # optional path/query
    )

    def __init__(self, rate_limit=10, circuit_threshold=5):
        self.request_history = []
        self.request_timestamps = []
        self.rate_limit = rate_limit
        self.circuit_threshold = circuit_threshold
        self.circuit_open = False
        self.circuit_tripped_at = 0
        self.consecutive_failures = 0

    def get(self, url, params=None, headers=None):
        return self._make_request(method='get', url=url, params=params, headers=headers)

    def post(self, url, data, params=None, headers=None):
        return self._make_request(method='post', url=url, params=params, headers=headers, data=data)

    def put(self, url, data, params=None, headers=None):
        return self._make_request(method='put', url=url, params=params, headers=headers, data=data)

    def patch(self, url, data, params=None, headers=None):
        return self._make_request(method='patch', url=url, params=params, headers=headers, data=data)

    def delete(self, url, params=None, headers=None):
        return self._make_request(method='delete', url=url, params=params, headers=headers)

    def _validate_url(self, url):
        if not self.API_URL_REGEX.fullmatch(url):
            raise APIRequestError(f"Invalid URL: {url}")

        return True

    def _check_rate_limit(self):
        window = 60
        current_time = int(time.time())
        one_minute_ago = current_time - window

        self.request_timestamps = [timestamp for timestamp in self.request_timestamps if timestamp > one_minute_ago ]

        if len(self.request_timestamps) >= self.rate_limit:
            raise RateLimitError("Rate limit exceeded. Please wait before making more requests.")

        self.request_timestamps.append(current_time)

    def _check_circuit_breaker(self):
        current_time = time.time()

        if self.circuit_open:
            if current_time - self.circuit_tripped_at > 30:
                self.circuit_open = False
                self.consecutive_failures = 0
            else:
                raise CircuitBreakerOpenError("Circuit breaker is open. Requests are temporarily blocked.")
        
    def _handle_failure(self):
        self.consecutive_failures += 1
        if self.consecutive_failures >= self.circuit_threshold:
            self.circuit_open = True
            self.circuit_tripped_at = time.time()

    def _handle_success(self):
        self.consecutive_failures = 0

    @retry_with_backoff(max_retries=3)
    def _make_request(self, method, url, params=None, headers=None, data=None):
        # Validate URL
        self._validate_url(url)

        # Check circuit breaker
        self._check_circuit_breaker()
        
        # Rate limiting tracking
        self._check_rate_limit()

        # start_time = time.time()
        start_time = time.perf_counter()
        http_status_code = None
        status = "failed"
        response_time = None
        error_message = ""
        json_data = None

        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                params=params,
                headers=headers,
                data=data,
                timeout=10
            )
            response_time = time.time() - start_time
            http_status_code = response.status_code

            response.raise_for_status()
            json_data = response.json()

            status = "success"
            self._handle_success()
            return json_data

        except requests.exceptions.Timeout as e:
            error_message = str(e)
            self._handle_failure()
            raise APITimeoutError(f"Request time out {e}")

        except requests.exceptions.RequestException as e:
            error_message = str(e)
            self._handle_failure()
            raise APIRequestError(f"API request failed: {e}")

        except (ValueError, requests.exceptions.JSONDecodeError) as e:
            error_message = "Failed to parse JSON payload"
            self._handle_failure()
            raise APIClientError(f"JSON Parsing Error: {e}")
        
        finally:
            if response_time  is None:
                response_time = time.perf_counter() - start_time

            history_log = {
                'url': url,
                'method': method.upper(),
                'http_status_code': http_status_code,
                'status': status,
                'timestamp': datetime.datetime.now(),
                'response_time': response_time,
                'error': error_message,
                'cache_hit': False
            }
            self.request_history.append(history_log)