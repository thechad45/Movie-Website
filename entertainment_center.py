# import fresh_tomatoes which will generate the html
import fresh_tomatoes

# import media which contains the class 'Movie'
import media

# instances of Movie begin here
the_iron_giant = media.Movie("The Iron Giant",
                        "A boy befriends a superweapon",
                        "https://upload.wikimedia.org/wikipedia/en/d/d3/The_Iron_Giant_poster.JPG",
                        "https://www.youtube.com/watch?v=obLtyj8hfFk")

gladiator = media.Movie("Gladiator",
                     "A war general is forced to fight his way up the ranks to free Rome",
                     "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                     "https://www.youtube.com/watch?v=ol67qo3WhJk")

tombstone = media.Movie("Tombstone", "A shoot-em-up featuring OK Corral",
                       "http://images.moviepostershop.com/tombstone-movie-poster-1993-1010259614.jpg",
                       "https://www.youtube.com/watch?v=XTWYKf5hXIg")

the_godfather = media.Movie("The Godfather", "Story of the rise of the Corleone crime family",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")
                            
anchorman = media.Movie("Anchorman", "A tale of the Channel 4 news team in San Diego",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=NJQ4qEWm9lU")

hot_rod = media.Movie("Hot Rod", "Rod decides to perform one big stunt to save his terminally ill stepfather",
                      "https://upload.wikimedia.org/wikipedia/en/7/7f/Hot-rod-poster.jpg",
                      "https://www.youtube.com/watch?v=DhdrA9qz79o")


# List of movies to be passed in to the open_movies_page function
movies = [the_iron_giant, gladiator, tombstone, the_godfather, anchorman, hot_rod]

# Call the function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)

