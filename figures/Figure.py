class Figure:
    
    def __init__(self, coord2D, index2D, typee, color):
        self.coord2D = coord2D
        self.index2D = index2D
        self.typee   = typee
        self.color   = color
        self.moved   = False
    
    def makeMove(self):
        raise NotImplementedError()
    
    # DEV util
    # -----------------------------------
    def print(self):
        print(
              "coord2D: " + str(self.coord2D) + "\n" +
              "index2D: " + str(self.index2D) + "\n" +
              "type   : " + self.typee        + "\n" +
              "color  : " + self.color
             )
    # -----------------------------------