from redis_rate_limiter import FixedWindowRateLimiter
import time

limiter = FixedWindowRateLimiter(max_requests=3, window=10)  # 3 requests per 10s

user = "1023"

for i in range(5):
    allowed = limiter.is_allowed(user)
    print(f"Request {i+1} for student {user}: {'Allowed' if allowed else 'Blocked'}")
    time.sleep(2)

