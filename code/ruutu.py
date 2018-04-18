class Ruutu():

	def __init__(self, is_wall = False):
		self.is_wall = is_wall 

	def is_wall_ruutu(self):
		return self.is_wall

	def is_empty(self):
		return not self.is_wall_ruutu()

	def set_wall(self):
		if self.is_empty():
			self.is_wall = True
			return True
		else:
			return False