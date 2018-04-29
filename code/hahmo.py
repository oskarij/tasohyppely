from PyQt5 import QtCore

from hahmographicsitem import HahmoGraphicsItem
from sijainti import Sijainti
from voitto import Voitto
import os, sys

#Sisältää hahmon toiminnan ja liikkeen päivityksen

class Hahmo():
	
	def __init__(self):
		self.maailma = None
		self.sijainti = None 
		self.graphics
		self.counter = 0
		self.gui = None
		self.time = 0

	def get_maailma(self):
		return self.maailma

	#asettaa hahmon maailmaan
	def set_maailma(self, maailma):
		if self.get_maailma() is not None:
			return False
		else:
			self.maailma = maailma
			self.sijainti = Sijainti(26,649)
			return True

	def get_sijainti(self):
		return self.sijainti

	def graphics(self, graphicsitem):
		self.graphics = graphicsitem

	def reset(self):
		self.sijainti = Sijainti(26,649)
		self.time = 0

	def add_gui(self,gui):
		self.gui = gui

	def update(self, keys_pressed):
		dx = 0
		if self.counter == 0:
			dy = 5
		
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
				self.counter = 10
		
		if self.counter != 0:
			dy = -10
			self.counter -= 1

		self.collision(dy)

		if QtCore.Qt.Key_R in keys_pressed:
			self.reset()

		self.graphics.update()

	#tarkistetaan, että hahmo on jonkin tason päällä
	def on_ground(self):
		self.sijainti.y += 1
		self.graphics.update()
		for i in self.maailma.esteet:
			ret = self.graphics.collidesWithItem(i.graphics)
			if ret == True:
				break
		self.sijainti.y -= 1
		return ret

	#hoitaa törmäyksentunnistuksen
	def collision(self, d):

		#x-suuntainen liike
		if d == 3 or d == -3:
			self.sijainti.x += d
			self.graphics.update()

			ret = self.graphics.collidesWithItem(self.maailma.maali)
			if ret == True:
				Voitto(self.time, self.maailma.pelaaja)

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
			#hyppy
			if d < 0:
				self.sijainti.y += d
				self.graphics.update()

				for i in self.maailma.esteet:
					ret = self.graphics.collidesWithItem(i.graphics)

					if ret == True:
						while ret == True:
							self.sijainti.y += 1
							self.graphics.update()
							ret = self.graphics.collidesWithItem(i.graphics)
						self.counter = 0		
			
			#putoaminen
			if self.on_ground() == False and d > 0:
				self.sijainti.y += d
				self.graphics.update()

				for i in self.maailma.esteet:
					ret = self.graphics.collidesWithItem(i.graphics)

					if ret == True:
						while ret == True:
							self.sijainti.y -= 1
							self.graphics.update()
							ret = self.graphics.collidesWithItem(i.graphics)

	def aika(self):
		self.time += 0.015