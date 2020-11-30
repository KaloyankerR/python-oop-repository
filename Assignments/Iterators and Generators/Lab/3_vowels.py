class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            letter = self.string[self.index]
            self.index += 1
            if self.is_vowel(letter):
                return letter
        raise StopIteration

    @staticmethod
    def is_vowel(letter):
        vowels = 'aeiuyo'
        return letter.lower() in vowels
