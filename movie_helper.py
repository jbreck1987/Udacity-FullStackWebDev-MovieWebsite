import webbrowser


class Movie():
    def __init__(self, title, mov_story,
                 trailer_youtube_url, poster_image_url):
        self.title = title
        self.mov_story = mov_story
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def __str__(self):
        return str('Movie Title: ' + self.title + '\n'
                   'Movie Story: ' + self.mov_story)

    def __repr__(self):
        return '{}.{}("{}","{}","{}","{}")'.format(
            self.__module__,
            "Movie",
            self.title,
            self.mov_story,
            self.trailer_youtube_url,
            self.poster_image_url)
