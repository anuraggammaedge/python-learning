from collections import Counter

class APIMetrics:
    def __init__(self):
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.total_response_time = 0
        self.cache_hits = 0
        self.cache_misses = 0
        self.rate_limit_violations = 0
        self.error_frequency = Counter()


    def record_success(self, response_time):
        self.successful_requests += 1
        self.total_requests += 1
        self.total_response_time += response_time

    def record_failure(self, error_type):
        self.failed_requests += 1
        self.total_requests += 1
        self.error_frequency[error_type] += 1

    def record_rate_limit_violation(self):
        self.rate_limit_violations += 1

    def record_cache_hit(self):
        self.cache_hits += 1

    def record_cache_miss(self):
        self.cache_misses += 1

    @property
    def average_response_time(self):
        if self.successful_requests == 0:
            return 0

        return (
            self.total_response_time / 
            self.successful_requests
        )
    @property
    def success_rate(self):
        if self.successful_requests == 0:
            return 0
        return (self.successful_requests/ self.total_requests) * 100
        
    @property
    def cache_hit_ratio(self):

        total_cache_requests = self.cache_hits + self.cache_misses
        if total_cache_requests == 0:
            return 0

        return (
            self.cache_hits / total_cache_requests
        ) * 100

    def generate_report(self):
        return {
            key : value 
            for key, value in {
                "total_requests": self.total_requests,
                "successful_requests": self.successful_requests,
                "failed_requests": self.failed_requests,
                "average_response_time": self.average_response_time,
                "success_rate": self.success_rate,
                "cache_hits": self.cache_hits,
                "cache_misses": self.cache_misses,
                "cache_hit_ratio": self.cache_hit_ratio,
                "rate_limit_violations": self.rate_limit_violations,
                "error_frequency": dict(self.error_frequency)
            }.items()
        }
