from PyQt5 import QtWidgets, QtGui, QtCore

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
		self.setPos(sijainti.x, sijainti.y)

	def updateColor(self):
		#muita värejä?
		color = QtGui.QColor(247,93,178)
		brush = QtGui.QBrush(color)
		self.setBrush(brush)

	#updatehp?