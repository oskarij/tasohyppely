class Ruutu():

	def __init__(self, is_wall = False):
		'''
		Luo ruudun maailmaan. Ruutu voi olla tyhjä, sisältää pelaajan tai seinän
		'''
		self.player = None #oletuksena ei ole pelaajaa
		self.is_wall = is_wall 

	def is_wall_ruutu(self):
		return self.is_wall

	def get_player(self):
		return self.player

	def is_empty(self):
		return not self.is_wall_ruutu() and self.player is None

	def set_wall(self):
		if self.is_empty():
			self.is_wall = True
			return True
		else:
			return False