def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            return res * times

        return wrapper

    return decorator
