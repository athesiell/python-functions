import time

def log(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        total = end_time - start_time

        # Write log message to log.txt

        with open("log.txt", "a") as f:
            f.write(f'{fn.__name__}; args: {args}; kwargs: {kwargs}; execution time: {total:.2f}')
            return result
    return wrapper


@log
def foo(a, b, c):
    return a + b + c

foo(1,2, c=3)