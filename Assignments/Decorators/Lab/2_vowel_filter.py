def vowel_filter(function):
    def wrapper(*args, **kwargs):
        letters = function(*args, **kwargs)
        return [x for x in letters if x in 'aeuio']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
