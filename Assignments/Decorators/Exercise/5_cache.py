def cache(function):
    log = {}

    def wrapper(arg):
        if arg not in log:
            res = function(arg)
            log[arg] = res
            return res
        return log[arg]

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
