class dictionary_iter:
    def __init__(self, expected_dict):
        self.dictionary = expected_dict
        self.dictionary_len = len(self.dictionary)
        self.keys = list(self.dictionary.keys())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.dictionary_len:
            key = self.keys[self.current_index]
            value = self.dictionary[key]
            self.current_index += 1
            return (key, value)
        raise StopIteration
