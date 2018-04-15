from PyQt5.QtWidgets import QApplication
import sys

from gui import GUI
from maailma import Maailma
from sijainti import Sijainti

def main():
	taso1 = Maailma()


	app = QApplication(sys.argv)
	gui = GUI(taso1, 25)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()