class Este():

	def __init__(self):
		self.koordinaatit = []

	def get_coordinates(self):
		return self.koordinaatit

	def add_coordinate(self, sijainti):
		self.koordinaatit.append(sijainti)
