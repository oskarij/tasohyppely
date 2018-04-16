from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI
from maailma import Maailma
from sijainti import Sijainti
from hahmo import Hahmo

def main():
	taso1 = Maailma()
	hahmo = Hahmo()
	height = taso1.get_height() - 2
	aloitussijainti = Sijainti(1, height)
	taso1.add_hahmo(hahmo, aloitussijainti)

	app = QApplication(sys.argv)
	gui = GUI(taso1, 25)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()