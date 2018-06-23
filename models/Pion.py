class Pion:

    def __init__(self, idPion, couleurPion, formePion, position_x, position_y, Joueur):
        self.idPion = idPion
        self.couleurPion = couleurPion
        self.formePion = formePion
        self.position_x = position_x
        self.position_y = position_y
        self.joueur = Joueur()

    def getIdPion(self):
        return self.idPion

    def getCouleurPion(self):
        return self.couleurPion

    def getFormePion(self):
        return self.formePion

    def getPosition_x(self):
        return self.position_x

    def getPosition_y(self):
        return self.position_y

    def getJoueur(self):
        return self.joueur

    def setIdPion(self, idPion):
        self.idPion = idPion

    def setCouleurPion(self, couleurPion):
        self.couleurPion = couleurPion

    def setCouleurPion(self, couleurPion):
        self.couleurPion = couleurPion

    def setFormePion(self, formePion):
        self.formePion = formePion

    def setPosition_x(self, position_x):
        self.position_x = position_x

    def setPosition_y(self, position_y):
        self.position_y = position_y

    def getJoueur(self, Joueur):
        self.joueur = Joueur

