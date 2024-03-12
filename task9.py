import functools

def validate(func):
    @functools.wraps(func)
    def wrapper(*args):
        if all(0 <= arg <=256 for arg in args):
            return func(*args)
        else:
            return 'Function call is not valid!'
    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return 'Pixel created!'

print(set_pixel(0, 127, 300))
print(set_pixel(0, 127, 255))