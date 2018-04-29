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


	#poistamalla demomaalin kommentin voi testata maaliinpääsemistä helpommin
	taso1.add_maali(Sijainti(400,26))  #oikea
	#taso1.add_maali(Sijainti(665,625)) #demo


	platform1 = taso1.add_wall(Sijainti(100,600), 100, 25)
	platform2 = taso1.add_wall(Sijainti(250,550), 75, 25)
	platform3 = taso1.add_wall(Sijainti(375,500), 50, 25)
	platform4 = taso1.add_wall(Sijainti(300,440), 25, 25)
	platform5 = taso1.add_wall(Sijainti(200,440), 25, 25)
	platform6 = taso1.add_wall(Sijainti(100,440), 25, 25)
	platform7 = taso1.add_wall(Sijainti(25,350), 50, 25)
	platform8 = taso1.add_wall(Sijainti(100,300), 500, 25)
	platform9 = taso1.add_wall(Sijainti(400,75), 75, 25)
	platform10 = taso1.add_wall(Sijainti(200,150), 25,150)
	platform11 = taso1.add_wall(Sijainti(125,200),5,5)
	platform12 = taso1.add_wall(Sijainti(525,225),25,25)
	platform13 = taso1.add_wall(Sijainti(625,175),25,25)
	platform14 = taso1.add_wall(Sijainti(523,150),25,25)
	platform15 = taso1.add_wall(Sijainti(375,25),25,75)

	app = QApplication(sys.argv)
	gui = GUI(taso1, taso1.esteet, app)

	gui.activate_exit()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()