class CelluleOqp(Cellule):

    def __init__(self, pion):
        super()._init_()
        self.pion = pion

    def get_pion(self):
        return self.pion

    def set_pion(self, pion):
        self.pion = pion