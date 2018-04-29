#tason "seinät"

class Este():

	def __init__(self, xy, width, height):
		self.x = xy.get_x()
		self.y = xy.get_y()
		self.width = width
		self.height = height
		self.graphics = None

		def get_x(self):
			return self.x

		def get_y(self):
			return self.y

		def get_width(self):
			return self.width

		def get_height(self):
			return self.height

	def add_graphics(self, graphicsitem):
		self.graphics = graphicsitem