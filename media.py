import webbrowser

class Movie():
	"The Movie class contains information and methods pertaining to a movie."
	def __init__(self, movie_title, movie_storyline, movie_image_url, movie_trailer_url, director, release_year):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_image_url
		self.trailer_youtube_url = movie_trailer_url
		self.director = director
		self.release_year = release_year

	def showTrailer():
		"Opens a modal box displaying the YouTube trailer for the specified movie."
		webbrowser.open(self.trailerUrl)
