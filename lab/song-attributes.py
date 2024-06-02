# SOLUTION 1
class Song:
    """
    A song.
    """
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, title, artist, genre):
        self.name = title
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if genre not in Song.genres:
            Song.genres.append(genre)
        if artist not in Song.artists:
            Song.artists.append(artist)
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1



# SOLUTION 2
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, title, artist, genre):
        self.name = title
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)
