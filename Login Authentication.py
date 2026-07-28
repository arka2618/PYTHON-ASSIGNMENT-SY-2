user_logged_in = False

def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user['user_logged_in']:
            print(f"Access denied: '{user.get('name', 'User')}' is not logged in.")
            return None
        else:
            print(f"Access accepted: '{user.get('name', 'User')}' is logged in.")
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def view_dashboard(user):
    print(f"Welcome {user['name']}, here is your dashboard.")

# Test
user1 = {"name": "Arka", "user_logged_in": True}
user2 = {"name": "Guest", "user_logged_in": False}

view_dashboard(user1)
view_dashboard(user2)
