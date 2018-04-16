class Ruutu():

	def __init__(self, is_wall = False):
		'''
		Luo ruudun maailmaan. Ruutu voi olla tyhjä, sisältää pelaajan tai seinän
		'''
		self.hahmo = None #oletuksena ei ole pelaajaa
		self.is_wall = is_wall 

	def is_wall_ruutu(self):
		return self.is_wall

	def get_hahmo(self):
		return self.hahmo

	def is_empty(self):
		return not self.is_wall_ruutu() and self.hahmo is None

	def set_wall(self):
		if self.is_empty():
			self.is_wall = True
			return True
		else:
			return False

	def set_hahmo(self, hahmo):
		if self.is_empty():
			self.hahmo = hahmo
			return True
		else:
			return False

	def remove_hahmo(self):
		removed_hahmo = self.get_hahmo()
		self.hahmo = None
		return removed_hahmo