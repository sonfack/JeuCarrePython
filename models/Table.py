class Table:

    listeJoueurs ={}
    joueurCourant =""

    def __init__(self, idTable, nomtable, listeJoueur, listeCellules):
        self.idTable = idTable
        self.nomTable = nomtable
        self.joueurs = listeJoueur
        self.cellule = listeCellules

    def getIdTable(self):
        return self.idTable

    def getNonTable(self):
        return self.nomTable

    def getJoueurs(self):
        return self.joueurs

    def getCellule(self):
        return self.cellule

    def setIdTable(self, idTable):
        self.idTable = idTable

    def setNomtable(self, nomTable):
        self.nomTable = nomTable

    def setJoueurs(self, joueur):
        self.joueurs = joueur

    def setCellule(self, cellule):
        self.cellule = cellule

    def executerMouvement(self, Move):

        if(Move.getJoueur()==self.joueurCourant):
        else:
            print("Veuillez attendre votre tour")


    def ajouterJoueur(self, joueur):
        pass

    def verifierStatut(self):
        pass

    def afficherResulat(self):
        pass

    def arreterJeu(self):
        pass