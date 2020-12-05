class PhotoAlbum():
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        # for idx, page in enumerate(self.photos):
        #     if len(page) < 4:
        #         page.append(label)
        #         return f'{label} photo added successfully on page {idx + 1} slot {len(page) + 1}'
        #     return 'No more free spots'

        for p in range(self.pages):
            if len(self.photos[p]) < 4:
                self.photos[p].append(label)
                ind = self.photos[p].index(label)
                return f'{label} photo added successfully on page {p + 1} slot {ind + 1}'
        return 'No more free spots'

    def display(self):
        result = []
        for page in self.photos:
            result.append('-' * 11)
            result.append(('[] ' * len(page)).rstrip(' '))
        result.append('-' * 11)
        return '\n'.join(result) + '\n'
        # return '\n'.join(['-' * 11 + '\n' + ''.join('[]' * len(page)) for page in self.photos])


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
