class reverse_iter:
    def __init__(self, iterator):
        self.iterator = iterator
        self.i = len(self.iterator)

    def __iter__(self):
        return self

    def __next__(self):
        self.i -= 1
        if self.i >= 0:
            return self.iterator[self.i]
        raise StopIteration
