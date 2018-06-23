class Move:


    def __init__(self, idMove, Table, Joueur, Pion):
        self.idMove = idMove
        self.table = Table
        self.joueur = Joueur
        self.pion = Pion

    def getIdMove(self):
        return self.idMove

    def getTable(self):
        return self.table

    def getJoueur(self):
        return self.joueur

    def getPion(self):
        return self.Pion

    def setIdMove(self, idMove):
        self.idMove = idMove

    def setTable(self, Table):
        self.table = Table

    def setJoueur(self, Joueur):
        self.joueur = Joueur

    def setPion(self, Pion):
        self.pion = Pion



