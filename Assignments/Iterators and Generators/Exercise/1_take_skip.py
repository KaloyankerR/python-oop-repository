# class take_skip:
#     def __init__(self, step: int, count: int):
#         self.step = step
#         self.count = count
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter < self.count:
#             step = self.step * self.counter
#             self.counter += 1
#             return step
#         raise StopIteration


def take_skip(start, end):
    current_num = 0
    for x in range(end):
        yield current_num
        current_num += start


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print()
numbers = take_skip(10, 5)
for number in numbers:
    print(number)

