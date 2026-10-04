from strategy import RateLimitStrategy


class RateLimiter:
    def __init__(self, strategy: RateLimitStrategy):
        self.strategy = strategy

    def allow_request(self, key: str) -> bool:
        return self.strategy.allow_request(key)
