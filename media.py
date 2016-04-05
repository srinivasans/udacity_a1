class Movie():
	"""
	Movie Class instance stores the Title, Storyline, Thumbnail 
	and Youtube URL of the Movie 

	Usage :

	movie = Movie(<title>,<storyline>,<thumbnail>,<yt_url>)

	"""
	def __init__(self,title,storyline,thumbnail,yt_url):
		self.title = title
		self.storyline = storyline
		self.thumbnail = thumbnail
		self.yt_url = yt_url


