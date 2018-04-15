from PyQt5 import 

class HahmoGraphicsItem(QtWidgets.QGraphicsEllipseItem):

	def __init__(self, hahmo, ruutu_size):
		super(HahmoGraphicsItem, self).__init__()

		self.hahmo = hahmo
		self.ruutu_size = ruutu_size
		brush GtGui.QBrush(1)
		self.setBrush(brush)
		
