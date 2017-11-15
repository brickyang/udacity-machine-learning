'''Provides Movie class.'''


class Movie(object):
    '''This class provides a way to store movie related information

    Attributes:
        VALID_RATINGS: A constant variable of the movie's rating.
        title: A string of the movie's title.
        storyline: A string of the movie's storyline.
        poster_image_url: A url format string of the movie's poster image.
        trailer_url: A url format string of the movie's trailer.
            If there is no trailer, this attributes could be an empty string ''.
    '''

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
