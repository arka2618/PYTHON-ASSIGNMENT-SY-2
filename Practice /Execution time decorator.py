import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {start}-{end}")
    return wrapper

@timer
def numbers():
    for i in range(1000000):
        pass
numbers()
