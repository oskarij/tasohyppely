from PyQt5 import QtWidgets, QtCore, QtGui
import sys

from hahmo import Hahmo
from hahmographicsitem import HahmoGraphicsItem

class GUI(QtWidgets.QMainWindow):

    def __init__(self, taso, esteet):
        super().__init__()
        self.taso = taso
        self.hahmo_graphics = None
        self.keys_pressed = set()
        self.esteet = esteet

        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.setGeometry(300, 200, 800, 800)
        self.mainmenu()
        
    def mainmenu(self):
        self.setWindowTitle('Main Menu')

        font = QtGui.QFont()
        font.setPointSize(20)
        
        self.peli = QtWidgets.QPushButton('Aloita peli', self)
        self.peli.move(250,275)
        self.peli.setFixedSize(300,100)
        self.peli.setFont(font)
        
        self.stats = QtWidgets.QPushButton('Pisteet', self)
        self.stats.move(250, 425)
        self.stats.setFixedSize(300,100)
        self.stats.setFont(font)

        self.exitbutton = QtWidgets.QPushButton('Exit', self)
        self.exitbutton.move(5,5)
        
        self.show()

        self.peli.clicked.connect(self.game)
        self.stats.clicked.connect(self.hiscores)

    def game(self):
        self.peli.hide()
        self.stats.hide()
        self.exitbutton.hide()
        self.setWindowTitle('Tasohyppely')

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
        self.show()

        self.add_esteet_items(self.esteet)
        self.add_hahmo_graphics_items()
        self.hahmo_graphics.update()

        self.timer = QtCore.QBasicTimer()
        self.timer.start(16,self)

    def hiscores(self):
        pass

    def add_esteet_items(self, esteet):
        for i in esteet:
            estegraphics = QtWidgets.QGraphicsRectItem(i.x, i.y, i.width, i.height)
            color = QtGui.QColor(0,0,0) 
            brush = QtGui.QBrush(color)
            estegraphics.setBrush(brush)
            i.add_graphics(estegraphics)
            self.scene.addItem(estegraphics)

    def add_hahmo_graphics_items(self):
        self.hahmo = self.taso.get_hahmo()

        hahmo_graphics = HahmoGraphicsItem(self.hahmo)
        self.hahmo.graphics(hahmo_graphics)
        self.hahmo_graphics = hahmo_graphics
        
        self.scene.addItem(hahmo_graphics)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.update_hahmo()
        self.scene.update()

    def update_hahmo(self):
        self.hahmo.update(self.keys_pressed)

    def activate_exit(self):
        self.exitbutton.clicked.connect(self.close)
