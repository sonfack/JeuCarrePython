class Table:
    listeJoueurs = {}
    joueurCourant = ""

    def __init__(self, idTable, nomtable, listeJoueur, listeCellules):
        self.idTable = idTable
        self.nomTable = nomtable
        self.joueurs = listeJoueur
        self.cellules = listeCellules

    def getIdTable(self):
        return self.idTable

    def getNonTable(self):
        return self.nomTable

    def getJoueurs(self):
        return self.joueurs

    def getGrille(self):
        return self.grille

    def setIdTable(self, idTable):
        self.idTable = idTable

    def setNomtable(self, nomTable):
        self.nomTable = nomTable

    def setJoueurs(self, joueur):
        self.joueurs = joueur

    def setCellule(self, cellule):
        self.cellules = cellule

    def executerMouvement(self, Move):
        pass

    def ajouterJoueur(self, joueur):
        self.listeJoueurs.append(joueur)

    def verifierStatut(self):
        pass

    def afficherResulat(self):
        pass

    def arreterJeu(self):
        pass
