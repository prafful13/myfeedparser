class Feedclass:

	def __init__(self, name, url):
		self.name = name
		self.url = url

	def display_feed_details(self):
		print self.name + " "
		print self.url + " "