import webbrowser
import requests


class Movie:
    """ This class stores the information on movie
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, youtube_trailer_url=""):
        self.title = movie_title
        url = "http://www.omdbapi.com/?t="+movie_title.replace(" ","+")+"&y=&plot=short&r=json"
        response = requests.get(url)
        r = response.json()
        self.storyline = r['Plot'].encode('utf-8')
        self.poster_image_url = r['Poster'].encode('utf-8')
        self.trailer_youtube_url = youtube_trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
