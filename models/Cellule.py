class Cellule:

    def __init__(self, idCellule, point_x, point_y, Table):
        self.idCellule = idCellule
        self.point_x = point_x
        self.point_y = point_y
        self.table = Table

    def getIdCellule(self):
        return  self.idCellule

    def getPoint_x(self):
        return self.point_x

    def getPoint_y(self):
        return self.point_y

    def getTable(self):
        return self.table


    def setIdCellule(self, idCellule):
        self.idCellule = idCellule

    def setPoint_x(self, point_x):
        self.point_x = point_x

    def setPoint_y(self, point_y):
        self.point_y = point_y

    def setTable(self, table):
        self.table = table

    