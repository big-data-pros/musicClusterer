class TrackModel:
    def __init__(self, title: str, artist_name: str, label_name: str, genre: str, 
                 country: str, release_date: str, spotify_url: str, image_url: str, 
                 popularity: int):
        self.title = title
        self.artist_name = artist_name
        self.label_name = label_name
        self.genre = genre
        self.country = country
        self.release_date = release_date
        self.popularity = popularity
        self.spotify_url = spotify_url
        self.image_url = image_url

    def __repr__(self):
        return f"TrackModel(title={self.title}, artist_name={self.artist_name}, " \
               f"label_name={self.label_name}, genre={self.genre}, country={self.country}, " \
               f"release_date={self.release_date}, popularity={self.popularity}, " \
               f"spotify_url={self.spotify_url}, image_url={self.image_url})"