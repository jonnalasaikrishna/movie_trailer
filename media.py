import webbrowser

class Movie():

    def __init__(self, title, year, poster_url, trailer_url):
        
        self.title = title
        self.year = year
        self.poster_url = poster_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_url)




