import datetime
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{datetime.datetime.now()} | Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    print(f"Hello, {name}!")

greet("Arka")
print(greet.__name__)
print(greet.__doc__)
