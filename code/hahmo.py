from PyQt5 import QtCore

from hahmographicsitem import HahmoGraphicsItem
from sijainti import Sijainti

class Hahmo():
	
	def __init__(self):
		self.maailma = None
		self.sijainti = None 
		self.dead = False
		self.graphics

	def get_maailma(self):
		return self.maailma

	def set_maailma(self, maailma):
		if self.get_maailma() is not None:
			return False
		else:
			self.maailma = maailma
			self.sijainti = Sijainti(26,449)
			return True

	def is_dead(self):
		return self.dead

	def revive(self):
		self.dead = True

	def get_sijainti(self):
		return self.sijainti

	def graphics(self, graphicsitem):
		self.graphics = graphicsitem

	def reset(self):
		self.sijainti = Sijainti(26,449)

	def update(self, keys_pressed):
		dx = 0
		dy = 0
		
		#x-suuntainen liike
		if QtCore.Qt.Key_A in keys_pressed:
			dx -= 3
		if QtCore.Qt.Key_D in keys_pressed:
			dx += 3

		self.collision(dx)
		
		#y-suuntainen liike
		if QtCore.Qt.Key_W in keys_pressed:
			ret = self.on_ground()
			if ret == True:
				pass

		#self.collision(dy)

		if QtCore.Qt.Key_R in keys_pressed:
			self.reset()

		self.graphics.update()

	def on_ground(self):
		self.sijainti.y += 1
		self.graphics.update()
		for i in self.maailma.esteet:
			ret = self.graphics.collidesWithItem(i.graphics)
			if ret == True:
				break
		self.sijainti.y -= 1
		return ret

	def collision(self, d):

		#x-suuntainen liike
		if d == 3 or d == -3:
			self.sijainti.x += d
			self.graphics.update()

			#iteroidaan läpi jokainen este tasossa
			for i in self.maailma.esteet:
				ret = self.graphics.collidesWithItem(i.graphics)
				
				#jos törmäys tapahtuu -> vähennetään sijaintia kunnes ei törmää enää
				if ret == True:
					while ret == True:
						if d == 3:
							self.sijainti.x -= 1
							self.graphics.update()
						else:
							self.sijainti.x += 1
							self.graphics.update()
						ret = self.graphics.collidesWithItem(i.graphics)

		#y-suuntainen liike
		else:
			pass
				
