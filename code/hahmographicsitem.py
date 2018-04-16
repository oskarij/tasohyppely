from PyQt5 import QtWidgets, QtGui, QtCore
from hahmo import Hahmo

class HahmoGraphicsItem(QtWidgets.QGraphicsEllipseItem):

	def __init__(self, hahmo, ruutu_size):
		super(HahmoGraphicsItem, self).__init__()

		self.hahmo = hahmo
		self.ruutu_size = ruutu_size
		brush = QtGui.QBrush(1)
		self.setBrush(brush)
		rect = QtCore.QRectF()
		rect.setWidth(ruutu_size)
		rect.setHeight(ruutu_size)
		self.setRect(rect)
		self.update()

	def update(self):
		self.updatePosition()
		self.updateColor()

	def updatePosition(self):
		sijainti = self.hahmo.get_sijainti()
		self.setPos(sijainti.x*self.ruutu_size, sijainti.y*self.ruutu_size)

	def updateColor(self):
		color = QtGui.QColor(255,255,0)
		brush = QtGui.QBrush(color)
		self.setBrush(brush)