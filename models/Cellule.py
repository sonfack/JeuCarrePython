import models

class Cellule:

    def __init__(self, row, col):
        self.row = row
        self.col = col


    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col

