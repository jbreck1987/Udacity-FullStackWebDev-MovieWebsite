import webbrowser


class Movie():
    def __init__(self, mov_title, mov_story, mov_youtube_url, mov_poster_url):
        self.mov_title = mov_title
        self.mov_story = mov_story
        self.mov_youtube_url = mov_youtube_url
        self.mov_poster_url = mov_poster_url

    def show_trailer(self):
        webbrowser.open(self.mov_youtube_url)
