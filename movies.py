import media
import fresh_tomatoes

# START Movie instance definitions
her = media.Movie("Her",
									"A lonely writer develops an unlikely relationship with his newly purchased operating system that's designed to meet his every need.",
									"http://ia.media-imdb.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
									"https://www.youtube.com/watch?v=WzV6mXIOVl4",
									"Spike Jonze",
									"2013")

goodfellas = media.Movie("Goodfellas",
												 "Henry Hill and his friends work their way up through the mob hierarchy.",
												 "http://ia.media-imdb.com/images/M/MV5BMTY2OTE5MzQ3MV5BMl5BanBnXkFtZTgwMTY2NTYxMTE@._V1_SX214_AL_.jpg",
												 "https://www.youtube.com/watch?v=qo5jJpHtI1Y",
												 "Martin Scorsese",
												 "1990")

the_shawshank_redemption = media.Movie("The Shawkshank Redemption",
																			 "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
																			 "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
																			 "https://www.youtube.com/watch?v=6hB3S9bIaco",
																			 "Frank Darabont",
																			 "1994")

annie_hall = media.Movie("Annie Hall",
												 "Neurotic New York comedian Alvy Singer falls in love with the ditsy Annie Hall.",
												 "http://ia.media-imdb.com/images/M/MV5BMTU1NDM2MjkwM15BMl5BanBnXkFtZTcwODU3OTYwNA@@._V1_SX214_AL_.jpg",
												 "https://www.youtube.com/watch?v=TBzHphcc2Jw",
												 "Woody Allen",
												 "1977")

the_usual_suspects = media.Movie("The Usual Suspects",
																 "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.",
																 "http://ia.media-imdb.com/images/M/MV5BMzI1MjI5MDQyOV5BMl5BanBnXkFtZTcwNzE4Mjg3NA@@._V1_SX214_AL_.jpg",
																 "https://www.youtube.com/watch?v=oiXdPolca5w",
																 "Bryan Singer",
																 "1995")

its_a_wonderful_life = media.Movie("It's a Wonderful Life",
																	 "An angel helps a compassionate but despairingly frustrated businessman by showing what life would have been like if he never existed.",
																	 "http://ia.media-imdb.com/images/M/MV5BMTMzMzY5NDc4M15BMl5BanBnXkFtZTcwMzc4NjIxNw@@._V1_SX214_AL_.jpg",
																	 "https://www.youtube.com/watch?v=LJfZaT8ncYk",
																	 "Frank Capra",
																	 "1946")
# /END Movie instance definitions

# list of movies to show on page
movies = [her, goodfellas, the_shawshank_redemption, annie_hall, the_usual_suspects, its_a_wonderful_life]

# opens movie trailer website in browser, using the 
#movies specified in the 'movies' array above
fresh_tomatoes.open_movies_page(movies)
