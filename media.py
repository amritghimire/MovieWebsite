import webbrowser
import requests


class Movie:
    """ This class stores the information on movie
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Constructor for Movie class
    def __init__(self, movie_title, youtube_trailer_url=""):
        """ store the information about movie for the instance
        Parameter: title of movie and link to trailer of movie on youtube
        """
        self.title = movie_title
        url = "http://www.omdbapi.com/?t="+movie_title.replace(" ","+")+"&y=&plot=short&r=json"
        # Retrieves the information on movie from api
        response = requests.get(url)
        r = response.json()
        self.storyline = r['Plot'].encode('utf-8')
        self.poster_image_url = r['Poster']
        self.trailer_youtube_url = youtube_trailer_url
