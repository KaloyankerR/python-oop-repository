class Album:
    name: str
    songs: list
    published: bool

    def __init__(self, name: str, songs=None):
        self.name = name
        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs
        
        self.published = False

    def add_song(self, song):
        songs = [s.name for s in self.songs]

        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return 'Cannot add songs. Album is published.'
        elif song.name in songs:
            return 'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return 'Cannot remove songs. Album is published.'

        songs = [s for s in self.songs if s.name == song_name]
        if songs:
            song = songs[0]
            self.songs.remove(song)
            return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        data = f'Album {self.name}\n'
        for song in self.songs:
            data += f'== {song.get_info()}\n'
        return data
