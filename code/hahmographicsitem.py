from PyQt5 import QtWidgets, QtGui, QtCore
from hahmo import Hahmo

class HahmoGraphicsItem(QtWidgets.QGraphicsEllipseItem):

	def __init__(self, hahmo, ruutu_size):
		super(HahmoGraphicsItem, self).__init__()

		self.hahmo = hahmo
		self.ruutu_size = ruutu_size
		brush = QtGui.QBrush(1)
		self.setBrush(brush)

		x = hahmo.get_sijainti().get_x()
		y = hahmo.get_sijainti().get_y()
		self.setRect(x*ruutu_size,y*ruutu_size,ruutu_size,ruutu_size)
		self.update()

	def update(self):
		self.updatePosition()
		self.updateColor()

	def updatePosition(self):
		sijainti = self.hahmo.get_sijainti()
		ruutu = self.hahmo.get_sijainti_ruutu().is_empty()
		if (ruutu == True):
			self.setPos(sijainti.x*self.ruutu_size, sijainti.y*self.ruutu_size)

	def updateColor(self):
		color = QtGui.QColor(255,255,0)
		brush = QtGui.QBrush(color)
		self.setBrush(brush)