import time

from strategy import RateLimitStrategy


class FixedWindowStrategy(RateLimitStrategy):
    def __init__(self, limit: int, window_size: int):
        self.limit = limit
        self.window_size = window_size
        self.requests = {}

    def allow_request(self, key: str) -> bool:
        current_time = time.time()

        if key not in self.requests:
            self.requests[key] = {
                "current_request_count": 1,
                "window_start": current_time,
            }
            return True

        data = self.requests[key]

        if current_time - data["window_start"] >= self.window_size:
            data["current_request_count"] = 1
            data["window_start"] = current_time
            return True

        if data["current_request_count"] < self.limit:
            data["current_request_count"] += 1
            return True

        return False
