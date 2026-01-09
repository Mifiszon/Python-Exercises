import time
from functools import wraps

def log_call(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "a") as f:
                f.write(f"[{timestamp}] {func.__name__}{args} -> {result}\n")
            return result
        return wrapper
    return decorator


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        durr = time.time() - start
        print(f"Czas wykonania {func.__name__}: {durr:.4f}s")
        return result
    return wrapper


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print(f"Funkcja {func.__name__} została wywołana {wrapper.calls} razy")
        return result
    wrapper.calls = 0
    return wrapper


def memorize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return wrapper
