class Band:
    name: str
    albums: list

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        albums_list = [x for x in self.albums if x.name == album.name]

        if album in albums_list:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        albums_list = [x for x in self.albums if x.name == album_name]

        if albums_list:
            album = albums_list[0]
            if album.published:
                return 'Album has been published. It cannot be removed.'
            self.albums.remove(album)
            return f'Album {album.name} has been removed.'

        return f'Album {album_name} is not found.'

    def details(self):
        data = f'Band {self.name}\n'
        for album in self.albums:
            data += f'{album.details()}'
        return data
