from math import sqrt
from itertools import count, islice


def get_primes(numbers):
    for num in numbers:
        if num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1))):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
