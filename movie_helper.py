import webbrowser


class Movie():
    """
    Defines Movie objects used to build a webpage
    containing informaton about Movie instances.


    Attributes:
        title: String of the title of the Movie.
        mov_story: String of a short summary of the Movie.
        trailer_youtube_url: URL of a video of the Movie trailer.
        poster_image_url: URL of an image of the Movie's cover art.
        """

    def __init__(self, title, mov_story,
                 trailer_youtube_url, poster_image_url):
        """Inits the Movie instance"""
        self.title = title
        self.mov_story = mov_story
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        """Opens the YouTube URL stored in the Movie instance."""
        webbrowser.open(self.trailer_youtube_url)

    def __str__(self):
        """String representation of the Movie instance"""
        return str('Movie Title: ' + self.title + '\n'
                   'Movie Story: ' + self.mov_story)

    def __repr__(self):
        """'Code' representation of the Movie instance"""
        return '{}.{}("{}", "{}", "{}", "{}")'.format(
            self.__module__,
            self.__class__.__name__,
            self.title,
            self.mov_story,
            self.trailer_youtube_url,
            self.poster_image_url)
