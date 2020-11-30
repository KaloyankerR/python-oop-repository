class sequence_repeat:
    def __init__(self, sequence: str, times: int):
        self.sequence = sequence
        self.times = times
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.times:
            if self.index == len(self.sequence) - 1:
                self.index = -1
            self.index += 1
            self.times -= 1
            return self.sequence[self.index]
        raise StopIteration
