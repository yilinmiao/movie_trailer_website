import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #define constructor/initialization method for class movie
    #constructor contains parameters: movie_title, box_art, trailer_link.
    def __init__(self, movie_title, box_art, trailer_link):
        self.title = movie_title
        self.poster_image_url = box_art
        self.trailer_youtube_url = trailer_link

