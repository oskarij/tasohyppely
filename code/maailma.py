from sijainti import Sijainti
from este import Este

class Maailma():

    def __init__ (self, koko):
        self.esteet = []
        self.hahmo = None
        self.size = koko
        self.set_borders()

    def get_width(self):
        return self.size

    def get_height(self):
        return self.size

    def add_wall(self, xy, width, height):
        este = Este(xy, width, height)
        self.esteet.append(este)
        return este

    def contains(self, sijainti):
        x_koordinaatti = sijainti.get_x()
        y_koordinaatti = sijainti.get_y()
        return 0 <= x_koordinaatti < self.get_width() and 0 <= y_koordinaatti < self.get_height()

    def add_hahmo(self, hahmo, sijainti):
        self.hahmo = hahmo
        ret = self.hahmo.set_maailma(self, sijainti)
        if ret == False:
            print("Hahmon lisäys ei onnistunut")

    def get_hahmo(self):
        return self.hahmo

    #asettaa tasolle ulkoseinät
    def set_borders(self):
        x = self.get_width()
        y = self.get_height()
        
        seinäL = Este(Sijainti(0,0), 25, 500)
        self.esteet.append(seinäL)

        seinäR = Este(Sijainti(475,0), 25, 500)
        self.esteet.append(seinäR)

        katto = Este(Sijainti(26,0), 448, 25)
        self.esteet.append(katto)

        lattia = Este(Sijainti(26, 475), 448, 25)
        self.esteet.append(lattia)
            
