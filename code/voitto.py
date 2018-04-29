from PyQt5 import QtWidgets, QtGui, QtCore
import os
import sys

from savestats import SaveStats

class Voitto():
	
	def __init__(self, aika, pelaaja):
		ds = (aika % 1)*100	
		minute = aika / 60

		self = QtWidgets.QMessageBox()
		self.setWindowTitle(" ")
		self.setGeometry(650,550,0,0)
		self.setText("Voitit pelin!")
		self.setInformativeText("Aikasi oli: \n{:2.0f} min {:2.0f} s {:2.0f} ms".format(minute,aika,ds))
		self.exec()

		SaveStats(aika, pelaaja)

		os.execl(sys.executable, sys.executable, *sys.argv)
