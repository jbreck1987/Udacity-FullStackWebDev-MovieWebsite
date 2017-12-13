import webbrowser


class Movie():
    def __init__(self, title, mov_story, trailer_youtube_url, poster_image_url):
        self.title = title
        self.mov_story = mov_story
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
