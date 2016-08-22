"""The main file for movie trailer website"""

import fresh_tomatoes
from media import Movie

# Create objects for movie
toy_story = Movie(movie_title="Toy Story",
                  youtube_trailer_url="https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar",
               "http://youtube.com/watch?v=5PSNL1qE6VY")
school_of_rocks = Movie("School of Rock",
                        "https://youtube.com/watch?v=3PsUJFEBC74")
ratatouille = Movie("Ratatouille",
                    "https://youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = Movie("Midnight in paris",
                          "https://youtube.com/watch?v=FAfR8omt-CY")

# create array of movies

movies = [Movie("Now you see me", "https://www.youtube.com/watch?v=4OtM9j2lcUA"),
          Movie("Kingsman", "https://www.youtube.com/watch?v=m4NCribDx4U"),
          Movie("Tomorrowland", "https://www.youtube.com/watch?v=1k59gXTWf-A"),
          Movie("The Last Stand", "https://www.youtube.com/watch?v=oc0x-jiewTE"),
          toy_story, avatar, school_of_rocks,
          ratatouille, midnight_in_paris]

# Parse the movies into html
fresh_tomatoes.open_movies_page(movies)
