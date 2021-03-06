import webbrowser


class Movie():  # define the class for movie instances
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):  # define constructor
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # test trailer url in browser
        webbrowser.open(self.trailer_youtube_url)
