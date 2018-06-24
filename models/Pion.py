import models

class Pion:

    def __init__(self, num, couleur, forme, x, y, joueur):
        self.num = num
        self.couleur = couleur
        self.forme = forme
        self.x = x
        self.y = y
        self.joueur = joueur

    def get_num(self):
        return self.num

    def get_couleur(self):
        return self.couleur

    def get_forme(self):
        return self.forme

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_joueur(self):
        return self.joueur

    def set_num(self, num):
        self.num = num

    def set_couleur(self, couleur):
        self.couleur = couleur

    def set_forme(self, forme):
        self.forme = forme

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_joueur(self, joueur):
        self.joueur = joueur

