logged_in = True

def require_login(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Please Login first")
    return wrapper

@require_login
def profile():
    print("Welcome to your Profile")
profile()
