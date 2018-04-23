from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI
from maailma import Maailma
from sijainti import Sijainti
from hahmo import Hahmo


MAAILMAN_KOKO = 500

def main():
	taso1 = Maailma(MAAILMAN_KOKO)
	hahmo = Hahmo()
	taso1.add_hahmo(hahmo)

	app = QApplication(sys.argv)
	gui = GUI(taso1, taso1.esteet)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()