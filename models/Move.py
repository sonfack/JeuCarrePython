import models

class Move:

    def __init__(self, num, table, joueur, pion, cellule):
        self.num = num
        self.table = table
        self.joueur = joueur
        self.pion = pion
        self.cellule = cellule

    def get_num(self):
        return self.num

    def get_table(self):
        return self.table

    def get_joueur(self):
        return self.joueur

    def get_pion(self):
        return self.pion

    def get_cellule(self):
        return  self.cellule

    def set_num(self, num):
        self.num = num

    def set_table(self, table):
        self.table = table

    def set_joueur(self, joueur):
        self.joueur = joueur

    def set_pion(self, pion):
        self.pion = pion

    def set_cellule(self, cellule):
        self.cellule = cellule
