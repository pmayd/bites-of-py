from functools import wraps


def make_html(element):

    def decorator(func):

        @wraps(func)
        def wrapper():
            return f'<{element}>{func()}</{element}>'

        return wrapper

    return decorator


if __name__ == "__main__":
    @make_html('p')
    def hello():
        return "hello"

    print(hello())

