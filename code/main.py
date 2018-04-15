from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI
from maailma import Maailma
from sijainti import Sijainti

def main():
	taso1 = Maailma()
	hahmo = Hahmo()
	aloitussijainti = Sijainti(x, taso1.get_height-1)
	taso1.add_hahmo(hahmo, sijainti)

	app = QApplication(sys.argv)
	gui = GUI(taso1, 25)


	sys.exit(app.exec_())
https://stackoverflow.com/questions/5207305/moving-a-qgraphicsitem-around-a-central-point-in-pyqt4
if __name__ == '__main__':
	main()