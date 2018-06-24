import random
import models

class Table:

    joueur_courant = models.Joueur()
    joueur_gagnant = models.Joueur()
    pion = models.Pion()
    succes = 0
    matched_h = []
    matched_v = []
    matched_d = []

    def __init__(self, num, nom, nombre):
        self.num = num
        self.nom = nom
        self.grille = []
        self.cellules = models.Cellule(nombre, nombre)
        self.joueurs = []

    def get_num_table(self):
        return self.num

    def get_nom_table(self):
        return self.nom

    def get_joueurs(self):
        return self.joueurs

    def set_num_table(self, num):
        self.num = num

    def set_nom_table(self, nom):
        self.nom = nom

    def set_joueurs(self, joueur):
        self.joueurs.append(joueur)

    def creer_cellules(self):
        for line in range(self.cellules.get_row()):
            self.grille.append([])
            for column in range(self.cellules.get_col()):
                self.grille.append([])

    def afficher_cellules(self):
        for cell in self.grille:
            print(cell)

    def initialiser_partie(self):

        if len(self.joueurs)== 2:
            i = random.randint(0, len(self.joueurs) - 1)
            self.joueur_courant = self.joueurs[i]
        else:
            print("En attente d un deuxieme joueur pour debuter la partie")

    def executer_mouvement(self, move):
       if self.joueur_courant==move.get_joueur() :
           if isinstance(models.CelluleVide, move.get_cellule()):
               x = move.get_cellule().get_row()
               y = move.get_cellule().get_col()
               c = models.CelluleOqp(x, y, move.get_pion())
           else:
               print("Cellule deja occupee, veuillez en choisir une autre")
       else:
           print("Veuillez attendre votre tour avant de jouer")


    def mise_a_jour_table(self, table):
        for line in range(self.cellules.get_row()):
            self.grille.append(table.cellules.get_row())
            for column in range(self.cellules.get_col()):
                self.grille.append(table.cellules.get_col())



    def ajouter_joueur(self, joueur):
        if len(self.joueurs) < 2 :
            self.set_joueurs(joueur)
        else:
            print("Cette table a deja 2 joueurs")

    def verifier(self):
        for i in range(len(self.grille)):
            for j in range(len(self.grille)):

                # Recherche verticale
                if(i, j) not in self.matched_v:

                    if j == len(self.grille) -1 or j == len(self.grille):

                        if self.grille[i][j]==self.grille[i][j+1] and self.grille[i][j]==self.grille[i][j+2] and self.grille[i][j]==self.grille[i][j+3] and self.grille[i][j]==self.grille[i][j+4]:
                            self.matched_v.extend([(i, j), (i, j+1), (i, j+2), (i, j+3), (i, j+4)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j]==self.grille[i][j-1] and self.grille[i][j]==self.grille[i][j+1] and self.grille[i][j]==self.grille[i][j+2] and self.grille[i][j]==self.grille[i][j+3]:
                            self.matched_v.extend([(i, j), (i, j - 1), (i, j + 1), (i, j +2), (i, j +3)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j]==self.grille[i][j-2] and self.grille[i][j]==self.grille[i][j-1] and self.grille[i][j]==self.grille[i][j+1] and self.grille[i][j]==self.grille[i][j+2]:
                            self.matched_v.extend([(i, j), (i, j - 2), (i, j - 1), (i, j +1), (i, j +2)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j]==self.grille[i][j-3] and self.grille[i][j]==self.grille[i][j-2] and self.grille[i][j]==self.grille[i][j-1] and self.grille[i][j]==self.grille[i][j+1]:
                            self.matched_v.extend([(i, j), (i, j - 3), (i, j - 2), (i, j - 1), (i, j+1)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j]==self.grille[i][j-4] and self.grille[i][j]==self.grille[i][j-3] and self.grille[i][j]==self.grille[i][j-2] and self.grille[i][j]==self.grille[i][j-1]:
                            self.matched_v.extend([(i, j), (i, j - 4), (i, j - 3), (i, j - 2), (i, j - 1)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()


                # Recherche horizontale

                if (i, j) not in self.matched_h:

                    if i == len(self.grille) - 1 or i == len(self.grille):

                        if self.grille[i][j] == self.grille[i+1][j] and self.grille[i][j] == self.grille[i+2][j] and self.grille[i][j] == self.grille[i+3][j] and self.grille[i][j] == self.grille[i+4][j]:
                            self.matched_h.extend([(i, j), (i+1, j), (i+2, j), (i+3, j), (i+4, j)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-1][j] and self.grille[i][j] == self.grille[i+1][j] and self.grille[i][j] == self.grille[i+2][j] and self.grille[i][j] == self.grille[i+3][j]:
                            self.matched_h.extend([(i, j), (i-1, j), (i+1, j), (i+2, j), (i+3, j)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-2][j] and self.grille[i][j] == self.grille[i-1][j] and self.grille[i][j] == self.grille[i+1][j] and self.grille[i][j] == self.grille[i+2][j]:
                            self.matched_h.extend([(i, j), (i-2, j), (i-1, j), (i+1, j), (i+2, j)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-3][j] and self.grille[i][j] == self.grille[i-2][j] and self.grille[i][j] == self.grille[i-1][j] and self.grille[i][j] == self.grille[i+1][j]:
                            self.matched_h.extend([(i, j), (i, j - 3), (i, j - 2), (i, j - 1), (i, j + 1)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-4][j] and self.grille[i][j] == self.grille[i-3][j] and self.grille[i][j] == self.grille[i-2][j] and self.grille[i][j] == self.grille[i-1][j]:
                            self.matched_h.extend([(i, i), (i-4, j), (i-3, j), (i-2, j), (i-1, j)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                # Recherche diagonale

                if (i, j) not in self.matched_d:
                    if i == len(self.grille) -1 or i == len(self.grille):
                        if self.grille[i][j] == self.grille[i+1][j+1] and self.grille[i][j] == self.grille[i+2][j+2] and self.grille[i][j] == self.grille[i+3][j+3] and self.grille[i+4][j+4]:
                            self.matched_d.extend([(i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3), (i+4, j+4)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-1][j-1] and self.grille[i][j] == self.grille[i+1][j+1] and self.grille[i][j] == self.grille[i+2][j+2] and self.grille[i][j] == self.grille[i+3][j+3]:
                            self.matched_d.extend([(i, j), (i-1, j-1), (i+1, j+1), (i+2, j+2), (i+3, j+3)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-2][j-2] and self.grille[i][j] == self.grille[i-1][j-2] and self.grille[i][j] == self.grille[i+1][j+1] and self.grille[i][j] == self.grille[i+2][j+2]:
                            self.matched_d.extend([(i, j), (i-2, j-2), (i-1, j-1), (i+1, j+1), (i+2, j+2)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-3][j-3] and self.grille[i][j] == self.grille[i-2][j-2] and self.grille[i][j] == self.grille[i-1][j-1] and self.grille[i][j] == self.grille[i+1][j+1]:
                            self.matched_d.extend([(i, j), (i-3, j - 3), (i-2, j - 2), (i-1, j - 1), (i+1, j + 1)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()

                        elif self.grille[i][j] == self.grille[i-4][j-4] and self.grille[i][j] == self.grille[i-3][j-3] and self.grille[i][j] == self.grille[i-2][j-2] and self.grille[i][j] == self.grille[i-1][j-1]:
                            self.matched_d.extend([(i, i), (i-4, j-4), (i-3, j-3), (i-2, j-2), (i-1, j-1)])
                            self.succes = +5
                            self.pion = self.grille[i][j].get_pion()


    def afficher_resulat(self):

        if (self.succes == 5):
            self.joueur_gagnant = self.pion.get_joueur()
            print("Le gagnant de la partie est " + self.joueur_gagnant)


    def arreterJeu(self):
        pass