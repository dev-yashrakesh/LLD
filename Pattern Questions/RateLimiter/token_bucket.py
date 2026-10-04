import time

from strategy import RateLimitStrategy

class TokenBucketStrategy(RateLimitStrategy):
    def __init__(self, capacity: int , refill_rate : int):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.requests ={}

    def allow_request(self, key: str) -> bool:
        current_time = time.time()
        if key not in self.requests:
            self.requests[key]={
                "token":self.capacity,
                "last_refill_time":current_time,
            }
        data = self.requests[key]
        elapsed_time = current_time - data["last_refill_time"]
        new_token =  self.refill_rate * elapsed_time

        data["token"] = min(self.capacity , data["token"] + new_token)
        data["last_refill_time"] = current_time
        if data["token"] >= 1:
            data["token"] -= 1
            return True
        return False