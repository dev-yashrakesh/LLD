from factory import RateLimiterFactory
from rate_limiter import RateLimiter


strategy = RateLimiterFactory.create("fixed_window", 5, 60)
rate_limiter = RateLimiter(strategy)

for i in range(10):
    print(rate_limiter.allow_request("User1"))
