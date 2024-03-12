from typing import Dict
import time
execution_time: Dict[str, float] = {}


def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        total = end_time - start_time
        execution_time[fn.__name__] = total
        return result
    return wrapper

@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b

print(func_add(10, 20))
print(execution_time['func_add'])