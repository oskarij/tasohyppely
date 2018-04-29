from PyQt5 import QtWidgets, QtCore, QtGui

#tason maali

class Maali(QtWidgets.QGraphicsRectItem):
	
	def __init__(self, sijainti):
		super(Maali, self).__init__()

		self.xy = sijainti
		self.sizey = 50
		self.sizex = 10

		rect = QtCore.QRectF()
		rect.setWidth(self.sizex)
		rect.setHeight(self.sizey)
		self.setRect(rect)

		self.setPos(self.xy.x, self.xy.y)

		color = QtGui.QColor(255,0,0)
		brush = QtGui.QBrush(color)
		self.setBrush(brush)