from PyQt5 import QtWidgets, QtGui, QtCore

#hoitaa hahmon piirtämisen

class HahmoGraphicsItem(QtWidgets.QGraphicsEllipseItem):

	def __init__(self, hahmo):
		super(HahmoGraphicsItem, self).__init__()

		self.hahmo = hahmo
		self.hahmo_size = 25
		
		brush = QtGui.QBrush(1)
		self.setBrush(brush)
		
		rect = QtCore.QRectF()
		rect.setWidth(self.hahmo_size)
		rect.setHeight(self.hahmo_size)
		self.setRect(rect)
		color = QtGui.QColor(247,93,178)
		brush = QtGui.QBrush(color)
		self.setBrush(brush)
		
		self.update()

	def update(self):
		self.updatePosition()
		#tähän mahdollisia hahmoon liittyviä päivitettäviä asioita

	def updatePosition(self):
		sijainti = self.hahmo.get_sijainti()
		self.setPos(sijainti.x, sijainti.y)