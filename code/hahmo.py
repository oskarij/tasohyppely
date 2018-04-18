from PyQt5 import QtCore

from hahmographicsitem import HahmoGraphicsItem
class Hahmo():
	
	def __init__(self):
		self.maailma = None
		self.sijainti = None #pikseleissä
		self.dead = False
		self.graphics

	def get_maailma(self):
		return self.maailma

	def set_maailma(self, maailma, sijainti):
		if self.get_maailma() is not None:
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
		#jos palautus on False, hahmo ei ole ruudussa.
		return self.get_maailma().get_ruutu(self.get_sijainti())

	def graphics(self, graphicsitem):
		self.graphics = graphicsitem

	def move(self, keys_pressed):
		x = 0
		y = 0
		if QtCore.Qt.Key_A in keys_pressed:
			x -= 3
		if QtCore.Qt.Key_D in keys_pressed:
			x += 3
		if QtCore.Qt.Key_W in keys_pressed:
			#tähän hyppy
			pass
		self.sijainti.x += x
		self.sijainti.y += y
		self.graphics.update()