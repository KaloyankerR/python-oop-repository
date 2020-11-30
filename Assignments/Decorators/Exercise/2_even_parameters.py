def even_parameters(function):
    def wrapper(*args):
        try:
            for x in args:
                if not x % 2 == 0:
                    return "Please use only even numbers!"
            res = function(*args)
            return res
        except TypeError:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

print()


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
