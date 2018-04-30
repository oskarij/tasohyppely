from PyQt5 import QtWidgets, QtCore, QtGui
import sys, os

from hahmo import Hahmo
from hahmographicsitem import HahmoGraphicsItem
from toptengraphics import TopTenGraphics

#hoitaa ohjelman grafiikan

class GUI(QtWidgets.QMainWindow):

    def __init__(self, maailma, esteet,app):
        super().__init__()
        self.maailma = maailma
        self.hahmo_graphics = None
        self.keys_pressed = set()
        self.esteet = esteet
        self.app = app
        self.top = None

        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.setGeometry(300, 200, 800, 800)
        self.mainmenu()
        
    #main menun piirtäminen
    def mainmenu(self):
        self.setWindowTitle('Main Menu')

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("WASD-näppäimillä liikutetaan.\nR-näppäimellä pelin uudelleenaloitus.")
        self.label.move(200,50)
        self.label.setFixedSize(400,300)
        fontlabel = QtGui.QFont()
        fontlabel.setPointSize(15)
        self.label.setFont(fontlabel)

        self.peli = QtWidgets.QPushButton('Aloita peli', self)
        self.peli.move(250,275)
        self.peli.setFixedSize(300,100)
        self.peli.setFont(font)
        
        self.stats = QtWidgets.QPushButton('Ajat', self)
        self.stats.move(250, 425)
        self.stats.setFixedSize(300,100)
        self.stats.setFont(font)

        self.exitbutton = QtWidgets.QPushButton('Sulje', self)
        self.exitbutton.move(5,5)
        
        self.show()

        self.peli.clicked.connect(self.game)
        self.stats.clicked.connect(self.hiscores)

    #pelin piirtäminen
    def game(self):
        self.peli.hide()
        self.stats.hide()
        self.exitbutton.hide()
        self.label.hide()

        text, okPressed = QtWidgets.QInputDialog.getText(self, " ","Nimesi:", QtWidgets.QLineEdit.Normal, "")
        while not okPressed:
            text, okPressed = QtWidgets.QInputDialog.getText(self, " ","Nimesi:", QtWidgets.QLineEdit.Normal, "")
        while text == '':
            text, okPressed = QtWidgets.QInputDialog.getText(self, " ","Nimesi:", QtWidgets.QLineEdit.Normal, "")
        self.maailma.add_pelaaja(text)

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
        self.timer.start(15,self)

    #parhaan 10 tulosten piirtäminen
    def hiscores(self):
        ajat = {}
        try:
            with open("sav.txt", "r")as f:
                lines = f.readlines()
                for line in lines:
                    arr = line.split("|")
                    ajat[arr[0]] = float(arr[1])
            asc = sorted(ajat.items(), key=lambda x: x[1])
        except FileNotFoundError:
            asc = []

        topten = []
        try:
            for i in range(10):
                topten.append(asc[i])
        except IndexError:
            pass

        if self.top == None:
            self.top = TopTenGraphics(topten)

        self.top.show()


    #lisää esteiden grafiikat
    def add_esteet_items(self, esteet):
        for i in esteet:
            estegraphics = QtWidgets.QGraphicsRectItem(i.x, i.y, i.width, i.height)
            if i.ansa == False:
                color = QtGui.QColor(0,0,0)
            else:
                color = QtGui.QColor(255,0,0) 
            brush = QtGui.QBrush(color)
            estegraphics.setBrush(brush)
            i.add_graphics(estegraphics)
            self.scene.addItem(estegraphics)
        if self.maailma.maali != None:
            self.scene.addItem(self.maailma.maali)

    #lisää hahmon grafiikat
    def add_hahmo_graphics_items(self):
        self.hahmo = self.maailma.get_hahmo()
        self.hahmo.add_gui(self)

        hahmo_graphics = HahmoGraphicsItem(self.hahmo)
        self.hahmo.graphics(hahmo_graphics)
        self.hahmo_graphics = hahmo_graphics
        
        self.scene.addItem(hahmo_graphics)

    #napin painallus
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    #napin irtipäästäminen
    def keyReleaseEvent(self, event):
        try:
            self.keys_pressed.remove(event.key())
        except KeyError:
            pass
            #jotkin toimintaan liittymättömät näppäimet aiheuttavat errorin

    #periodisesti päivitettävät asiat
    def timerEvent(self, event):
        self.update_hahmo()
        self.scene.update()
        self.hahmo.aika()

    def update_hahmo(self):
        self.hahmo.update(self.keys_pressed)

    def activate_exit(self):
        self.exitbutton.clicked.connect(self.close)
