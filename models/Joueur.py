class Joueur:

    coup = 0

    def __init__(self, idJoueur, nomJoueur):
        self.idJoueur = idJoueur
        self.nomJoueur = nomJoueur

    def getIdJoueur(self):
        return self.idJoueur

    def getNomJoueur(self):
        return self.nomJoueur

    def setIdJoueur(self, idJoueur):
        self.idJoueur = idJoueur

    def setNomJoueur(self, nomJoueur):
        self.nomJoueur = nomJoueur

    def demanderJeu(self, Table):
        pass

    def mettreJeuEnPause(self, Table):
        pass

    def arreterJeu(self, Table):
        pass

    def jouerJeu(self, Move):
        self.coup = self.coup + 1
        pass
