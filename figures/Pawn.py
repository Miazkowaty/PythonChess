from .Figure import Figure


class Pawn(Figure):
    
    def __init__(self, coord2D, index2D, color):
        typee = "P"
        Figure.__init__(self, coord2D, index2D, typee, color)

    def makeMove(self, coord2D, index2D):
        move_x = index2D[0] - self.index2D[0]
        move_y = index2D[1] - self.index2D[1]
        if(
           (abs(move_x) == 0 and abs(move_y) == 1                        ) or
           (abs(move_x) == 0 and abs(move_y) == 2 and self.moved == False)
          ): 
            self.coord2D = coord2D
            self.index2D = index2D
            return True
        else:
            print("wrong move")
            return False