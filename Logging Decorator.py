def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@logger
def student():
    print("Welcome Students")
student()