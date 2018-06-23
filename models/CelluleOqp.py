class CelluleOqp(Cellule):


    def __init__(self, Pion):

        super().__init__()
        self.pion = Pion

    def getPoint(self):
        return self.pion

    def setPoint(self, Pion):
        self.pion = Pion