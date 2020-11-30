def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        numbers = []
        for x in seq:
            if len(numbers) == n:
                return numbers
            numbers.append(x)

    return (take, halves, integers)
