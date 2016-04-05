from media import Movie
import fresh_tomatoes


class EntertainmentCenter():
	def __init__(self,filename):
		self.filename=filename
		self.movies=[]
		f=open(self.filename,"r")
		for line in f:
			mov = line.split("\t")
			self.movies.append(Movie(mov[0],mov[1],mov[2],mov[3]))
		f.close()
		self.open()

	def open(self):
		fresh_tomatoes.open_movies_page(self.movies)


if __name__=="__main__":
	EntertainmentCenter("movies.tsv")



