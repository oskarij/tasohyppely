
class Hahmo():
	
	def __init__(self):
		self.maailma = None
		self.sijainti = None
		self.dead = False

	def get_maailma(self):
		return self.maailma

	def set_maailma(self, maailma, sijainti):
		target_ruutu = maailma.get_ruutu(sijainti)
		if (target_ruutu.get_hahmo() != self) or self.get_maailma() is not None:
			return False
		else:
			self.maailma = maailma
			self.sijainti = sijainti
			return True

	def is_dead(self):
		return self.dead

	def revive(self):
		self.dead = True

	def get_sijainti(self):
		return self.sijainti

	def get_sijainti_ruutu(self):
		return self.get_maailma().get_ruutu(self.get_sijainti())

	#luo hahmon liikutus
	def move(self, suunta):
		pass