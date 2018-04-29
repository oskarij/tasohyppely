from PyQt5 import QtWidgets, QtGui


class TopTenGraphics(QtWidgets.QWidget):

    def __init__(self,topten):
        super().__init__()
        self.list = [None] * 10
        self.topten = topten
        self.positions = {0:(90,50),1:(90,80),2:(90,110),3:(90,140),\
        4:(90,170),5:(90,200),6:(90,230),7:(90,260),8:(90,290),9:(90,320)}
        self.font = QtGui.QFont()
        self.font.setPointSize(13)

        self.setWindowTitle("10 parasta")
        self.setGeometry(450,350,500,400)

        self.exitbutton = QtWidgets.QPushButton('Sulje', self)
        self.exitbutton.move(5,5)
        self.exitbutton.clicked.connect(self.close)
        
        length = len(topten)

        for i in range(length):
            self.list[i] = self.topten[i]

        self.setlabel(0)
        self.setlabel(1)
        self.setlabel(2)
        self.setlabel(3)
        self.setlabel(4)
        self.setlabel(5)
        self.setlabel(6)
        self.setlabel(7)
        self.setlabel(8)
        self.setlabel(9)

    def setlabel(self,nro):
        try:
            nimi = self.list[nro][0]
            if len(nimi) > 10:
                nimi = (nimi[:10] + '...')

            aika = self.list[nro][1]
            ds = (aika % 1)*100 
            minute = aika / 60
            sekunti = str(aika)
            s1 = sekunti.split(".")[0]
            label = QtWidgets.QLabel(self)
            label.setText("{:d}. {:s} - {:2.0f} min {:s} s {:2.0f} ms".format((nro+1),nimi,minute,s1,ds))
            label.move(self.positions[nro][0],self.positions[nro][1])
            label.setFont(self.font)

        except TypeError:
            label = QtWidgets.QLabel(self)
            label.setText("{:d}.".format((nro+1)))
            label.move(self.positions[nro][0],self.positions[nro][1])
            label.setFont(self.font)