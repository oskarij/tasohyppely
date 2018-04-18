from ruutu import Ruutu
from ruutusijainti import ruutuSijainti
from sijainti import Sijainti

class Maailma():

    def __init__ (self):
        
        #10x10 ruudukko
    
        self.squares = [None] * 20
        for x in range(20):      
            self.squares[x] = [None] * 20
            for y in range(20):   
                self.squares[x][y] = Ruutu()  
        self.hahmo = None
        self.set_borders()

    def get_width(self):

        return len(self.squares)

    def get_height(self):
  
        return len(self.squares[0])

    def get_ruutu(self, ruutusijainti):
        #palauttaa ruutu-olion kyseisessä sijainnissa
        if self.contains(ruutusijainti):
            return self.squares[ruutusijainti.get_x()][ruutusijainti.get_y()]
        else:
            return False

    def add_wall(self, ruutusijainti):
        return self.get_ruutu(ruutusijainti).set_wall()

    def contains(self, ruutusijainti):
        x_koordinaatti = ruutusijainti.get_x()
        y_koordinaatti = ruutusijainti.get_y()
        return 0 <= x_koordinaatti < self.get_width() and 0 <= y_koordinaatti < self.get_height()

    def add_hahmo(self, hahmo, sijainti):
    	self.hahmo = hahmo
    	ret = self.hahmo.set_maailma(self,sijainti)
    	if ret == False:
    		print("Hahmon lisäys ei onnistunut")

    def get_hahmo(self):
    	return self.hahmo

    #asettaa tasolle 
    def set_borders(self):
        x = self.get_width()
        y = self.get_height()

        for i in range(x):
            location1 = ruutuSijainti(i, 0)
            location2 = ruutuSijainti(i, (y-1))
            self.add_wall(location1)
            self.add_wall(location2)
     
        for i in range(y):
            location1 = ruutuSijainti(0, i)
            location2 = ruutuSijainti((x-1), i)
            self.add_wall(location1)
            self.add_wall(location2)
