class produkty:
    def __init__(self, nazwa, bialko, tluszcze, weglowodany):
        self.N = nazwa
        self.B = bialko
        self.T = tluszcze
        self.W = weglowodany
        self.K = (self.B*4)+(self.T*9)+(self.W*4)
    
    def produkt(self):
        return{
            "nazwa": self.N,
            "bialko": self.B,
            "tluszcze": self.T,
            "weglowodany": self.W
        }