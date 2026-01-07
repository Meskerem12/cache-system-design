import redis
import time

class FixedWindowRateLimiter:
    def __init__(self, redis_host="localhost", redis_port=6379, max_requests=5, window=60):
        """
        max_requests: allowed requests per window
        window: time window in seconds
        """
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=0)
        self.max_requests = max_requests
        self.window = window

    def is_allowed(self, user_id):
        """
        Returns True if allowed, False if limit exceeded
        """
        key = f"rate:{user_id}"
        current = self.redis.get(key)

        if current is None:
            # First request → set counter
            self.redis.set(key, 1, ex=self.window)
            return True
        elif int(current) < self.max_requests:
            self.redis.incr(key)
            return True
        else:
            # Limit exceeded
            return False
