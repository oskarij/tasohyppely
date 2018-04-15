from ruutu import Ruutu
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

    def get_ruutu(self, sijainti):
        #palauttaa ruutu-olion kyseisessä sijainnissa
        #jos ruutua ei ole - palauttaa ruutu-objektin, joka ei sisälly tasoon
        if self.contains(sijainti):
            return self.squares[sijainti.get_x()][sijainti.get_y()]
        else:
            return Ruutu(True)

    def add_wall(self, sijainti):
        return self.get_square(sijainti).set_wall()

    def contains(self, sijainti):
        x_koordinaatti = sijainti.get_x()
        y_koordinaatti = sijainti.get_y()
        return 0 <= x_koordinaatti < self.get_width() and 0 <= y_koordinaatti < self.get_height()

    def add_hahmo(self, hahmo, sijainti):
    	self.hahmo = hahmo
    	self.get_ruutu(sijainti).set_hahmo(hahmo)

    def get_hahmo(self):
    	return self.hahmo

    #asettaa tasolle 
    def set_borders(self):
        x = self.get_width()
        y = self.get_height()

        for i in range(x):
            location1 = Sijainti(i, 0)
            location2 = Sijainti(i, (y-1))
            self.add_wall(location1)
            self.add_wall(location2)
     
        for i in range(y):
            location1 = Sijainti(0, i)
            location2 = Sijainti((x-1), i)
            self.add_wall(location1)
            self.add_wall(location2)
