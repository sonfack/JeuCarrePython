class Move:


    def __init__(self, idMove, Table, Move):
        self.idMove = idMove
        self.table = Table
        self.move = Move

    def getIdMove(self):
        return self.idMove

    def getTable(self):
        return self.table

    def getMove(self):
        return self.move
