from media import Movie
import fresh_tomatoes


class EntertainmentCenter():
	"""
	EntertainmentCenter Class instance generates movie database from file 
	and uses open function to open the datasets on a webpage

	Usage :

	ent_center = EntertainmentCenter(<filename>)

	"""
	def __init__(self,filename):
		self.filename=filename
		self.movies=[]
		#Loads movies text as Movie objects from file
		f=open(self.filename,"r")
		for line in f:
			mov = line.split("\t")
			self.movies.append(Movie(mov[0],mov[1],mov[2],mov[3]))
		f.close()
		self.open()

	def open(self):
		"""
		Function to open the movie database on webpage using fresh_tomatoes template
		"""
		fresh_tomatoes.open_movies_page(self.movies)


if __name__=="__main__":
	# Uses movie dataset filename as input to generate an HTML file and open it in the browser.
	EntertainmentCenter("movies.tsv")



