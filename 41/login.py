from functools import wraps


known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = args[0] if args else None

        if user not in known_users:
            return 'please create an account'

        elif user not in loggedin_users:
            return 'please login'

        else:
            return func(*args, **kwargs)
    
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'


if __name__ == "__main__":
    print(welcome('sue'))