from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI
from maailma import Maailma
from sijainti import Sijainti
from hahmo import Hahmo


RUUTUJENKOKO = 25

def main():
	taso1 = Maailma()
	hahmo = Hahmo()
	height = taso1.get_height() - 2
	aloitussijainti = Sijainti(1*RUUTUJENKOKO, height*RUUTUJENKOKO)
	taso1.add_hahmo(hahmo, aloitussijainti)

	app = QApplication(sys.argv)
	gui = GUI(taso1, RUUTUJENKOKO)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()