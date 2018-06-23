class Table:

    listeJoueurs ={}
    joueurCourant =""

    def __init__(self, idTable, nomtable, liste):
        self.idTable = idTable
        self.nomTable = nomtable
        self.joueurs = Joueur(liste)
        self.grille = [[]]

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

    def setGrille(self, grille):
        self.grille = grille

    def executerMouvement(self, Move):

        if(Move.getJoueur()==self.joueurCourant):

            if(not self.grille[Move.getPion().getPosition_x][Move.getPion().getPosition_y]):

                self.grille[Move.getPion().getPosition_x][Move.getPion().getPosition_y].append(Move.getPion())

                self.verifierStatut()


            else:
                print("Choix non disponible veuillez choisir une autre cellule")

        else:
            print("Veuillez attendre votre tour")

        pass

    def ajouterJoueur(self, joueur):
        self.listeJoueurs.append(joueur)

    def verifierStatut(self):
        pass

    def afficherResulat(self):
        pass

    def arreterJeu(self):
        pass