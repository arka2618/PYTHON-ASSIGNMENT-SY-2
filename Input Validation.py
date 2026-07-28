def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function '{func.__name__}' has been called {wrapper.calls} time(s).")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
