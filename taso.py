class Taso():

    def __init__ (self):
        
        #10x10 ruudukko
    
        self.squares = [None] * 10
        for x in range(10):      
            self.squares[x] = [None] * 10
            for y in range(10):   
                self.squares[x][y] = Square()    
        self.turn = 0                         

    def get_width(self):

        return len(self.squares)


    def get_height(self):
  
        return len(self.squares[0])

    def get_square(self, sijainti):
        #palauttaa ruutu-olion kyseisessä sijainnissa
        #jos ruutua ei ole - palauttaa ruutu-objektin, joka ei sisälly tasoon
        if self.contains(sijainti):
            return self.squares[sijainti.get_x()][sijainti.get_y()]
        else:
            return Square(True)

    def add_wall(self, sijainti):
        return self.get_square(location).set_wall()

    def contains(self, sijainti):
        x_koordinaatti = sijainti.get_x()
        y_koordinaatti = sijainti.get_y()
        return 0 <= x_koordinaatti < self.get_width() and 0 <= y_koordinaatti < self.get.get_height()
        