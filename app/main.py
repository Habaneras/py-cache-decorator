from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    # Separate cache store for this specific decorated function
    memo = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a hashable composite key from args and sorted kwargs
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in memo:
            print("Getting from cache")
            return memo[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[cache_key] = result
        return result

    return wrapper
