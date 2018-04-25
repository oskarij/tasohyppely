from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI
from maailma import Maailma
from sijainti import Sijainti
from hahmo import Hahmo
from este import Este


MAAILMAN_KOKO = 500

def main():
	taso1 = Maailma(MAAILMAN_KOKO)
	hahmo = Hahmo()
	taso1.add_hahmo(hahmo)

	platform1_coor = Sijainti(100,400)
	platform1 = taso1.add_wall(platform1_coor, 100, 25)

	app = QApplication(sys.argv)
	gui = GUI(taso1, taso1.esteet)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()