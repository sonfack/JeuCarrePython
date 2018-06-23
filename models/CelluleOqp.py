class CelluleOqp(Cellule):


    def __init__(self, Point):

        super().__init__()
        self.point = Point

    def getPoint(self):
        return self.point

    def setPoint(self, Point):
        self.point = Point