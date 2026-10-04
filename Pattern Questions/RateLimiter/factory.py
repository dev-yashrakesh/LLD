from fixed_window import FixedWindowStrategy


class RateLimiterFactory:
    @staticmethod
    def create(strategy_type: str, limit: int, window_size: int):
        if strategy_type == "fixed_window":
            return FixedWindowStrategy(limit, window_size)
        raise ValueError("Invalid strategy type")
