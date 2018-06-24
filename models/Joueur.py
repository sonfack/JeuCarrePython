import models

class Joueur:

    coup = 0

    def __init__(self, num, nom):
        self.num = num
        self.nom = nom
        self.table = models.Table()

    def get_num(self):
        return self.num

    def get_nom(self):
        return self.nom

    def get_table(self):
        return self.table

    def set_num(self, num):
        self.num = num

    def set_nom(self, nom):
        self.nom = nom

    def set_table(self, table):
        self.table = table

    def connexion_table(self, table):
        pass

    def jouer(self, move):
        self.coup = self.coup + 1
