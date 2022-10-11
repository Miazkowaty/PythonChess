from .Figure import Figure


class Queen(Figure):
    
    def __init__(self, coord2D, index2D, color):
        typee = "Q"
        Figure.__init__(self, coord2D, index2D, typee, color)

    def move(self, coord2D, index2D):
        move_x = index2D[0] - self.index2D[0]
        move_y = index2D[1] - self.index2D[1]
        if(
           (abs(move_x) == abs(move_y) and abs(move_x) > 0) or
           (
            (abs(move_x) > 0 and abs(move_y) == 0) or
            (abs(move_x) == 0 and abs(move_y) > 0)
           )
          ): 
            self.coord2D = coord2D
            self.index2D = index2D
            return True
        else:
            print("wrong move")
            return False