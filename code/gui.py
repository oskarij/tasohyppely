from PyQt5 import QtWidgets, QtCore, QtGui
import sys

from hahmo import Hahmo
from hahmographicsitem import HahmoGraphicsItem

class GUI(QtWidgets.QMainWindow):

    def __init__(self, taso, ruutu_size):
        super().__init__()
        self.taso = taso
        self.ruutu_size = ruutu_size
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.init_window()
        self.hahmo_graphics = None

        self.add_maailma_grid_items()
        self.add_hahmo_graphics_items()
        self.update_hahmo()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_hahmo)
        self.timer.start(10) 


    def init_window(self):
        
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Tasohyppely')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    def add_maailma_grid_items(self):
        width = self.taso.get_width()
        height = self.taso.get_height()

        for x in range(width):
            for y in range(height):
                square = QtWidgets.QGraphicsRectItem(x*self.ruutu_size,y*self.ruutu_size,self.ruutu_size,self.ruutu_size)
                if self.taso.squares[x][y].is_wall_ruutu() == False:
                    vari = QtGui.QColor(255,255,255) 
                    brush = QtGui.QBrush(vari)
                    #disable comments for no edges on squares
                    #pen = QtGui.QPen(vari)
                    #square.setPen(pen)
                    square.setBrush(brush)
                    self.scene.addItem(square)
                else:
                    vari = QtGui.QColor(20,20,20,255)
                    brush = QtGui.QBrush(vari)
                    square.setBrush(brush)
                    self.scene.addItem(square)

    def add_hahmo_graphics_items():
    	hahmo = self.taso.get_hahmo()
    	hahmo_graphics = HahmoGraphicsItem(hahmo, self.ruutu_size)
    	self.hahmo_graphics = hahmo_graphics
    	self.scene.addItem(hahmo_graphics)


    def update_hahmo(self):
    	self.hahmo_graphics.update()