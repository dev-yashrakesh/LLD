from abc import ABC, abstractmethod
import time


class RateLimitStrategy(ABC):
    @abstractmethod
    def allow_request(self , key:str)->bool:
        pass


class FixedWindowStrategy(RateLimitStrategy):

    def __init__(self , limit : int , window_size : int):
        self.limit = limit
        self.window_size = window_size
        self.requests = {}

    def allow_request(self , key:str)->bool:
        current_time = time.time()

        # first request of this user
        if key not in self.requests:
            self.requests[key] = {
                "current_request_count" : 1,
                "window_start" : current_time,
            }
            return True

        data =self.requests[key]
        print(data)
        # existing user refresh request
        if current_time - data["window_start"] >= self.window_size:
            data["current_request_count"] = 1
            data["window_start"] = current_time
            return True

        # increasing count of request within time
        if data["current_request_count"] < self.limit:
            data["current_request_count"] += 1
            return True

        # Exceeding request
        return False

class RateLimiterFactory:

    @staticmethod
    def create(strategy_type : str , limit : int , window_size : int):
        if strategy_type == "fixed_window":
            return FixedWindowStrategy(limit , window_size)
        else :
            raise ValueError("Invalid strategy type")

class RateLimiter:
    def __init__(self, strategy:RateLimitStrategy ):
        self.strategy = strategy

    def allow_request(self , key:str)->bool:
        return strategy.allow_request( key )

strategy = RateLimiterFactory.create(
    "fixed_window",
    5,
    60
)

rate_limiter = RateLimiter(strategy)

for i in range(10):
    print(rate_limiter.allow_request("User1"))