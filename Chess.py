import math
import os

from figures.Pawn   import Pawn
from figures.Rook   import Rook
from figures.Knight import Knight
from figures.Bishop import Bishop
from figures.Queen  import Queen
from figures.King   import King

white = "white"
black = "black"


class Tile:
    
    def __init__(self, coord2D, figOn, figColor):
        self.coord2D  = coord2D
        self.figOn    = figOn
        self.figColor = figColor
    
    def update(self, figOn, figColor):
        self.figOn    = figOn
        self.figColor = figColor

    # DEV util
    # -----------------------------------
    def print(self):
        print(
              "{"  + str(self.letter)   +
              ", " + str(self.index)    +
              ", " + str(self.figOn)    +
              ", " + str(self.figColor) +
              "}", end = ""
             )
    # -----------------------------------


class Board:
    
    def __init__(self):
        self.dim = 8
        
        self.indexes18 = list(range(1, self.dim + 1))                                   # 1) For rows counted as <from 1 to 8> for <from a to h>: [left-bottom -> right-top]
        self.indexes07 = list(range(0, self.dim))                                       # 2) For rows as in 2D table: [left-top -> right-bottom]
        self.letters   = ["a", "b", "c", "d", "e", "f", "g", "h"]
        
        self.indexes18_to_letters_Map = dict(zip(self.indexes18, self.letters))         # Ad. 1) <-
        self.letters_to_indexes07_Map = dict(zip(self.letters, self.indexes07))         # Ad. 2) <-
        
        self.tiles = []
        for hor in range(self.dim, 0, -1):
            row = []
            for ver in range(1, self.dim + 1):
                row.append(Tile(tuple((self.indexes18_to_letters_Map.get(ver), hor)), None, None))
            self.tiles.append(row)

    def getTileByCoord2D(self, coord2D):
        foundTile = False
        
        for row in self.tiles:
            for tile in row:
                if(tile.coord2D == coord2D):
                    foundTile = True
                    return tile
                
        if(not foundTile):
            print("nie znaleziono tile'a o podanych koordynatach")
            return None
                

class Player:
    
    def __init__(self, color):
        self.color = color


class Players:
    
    def __init__(self):
        self.players = (Player(white), Player(black))
        self.hasMove = 0
        self.winner  = None
        
    def changeTurn(self):
        self.hasMove = abs(self.hasMove - 1)


class Chess:
    
    def __init__(self):
        self.board   = Board()
        self.players = Players()
        
        self.whiteFigs = [
            Pawn  (tuple(("a", 2)), self.coord2D_to_index2D(tuple(("a", 2))), white),
            Pawn  (tuple(("b", 2)), self.coord2D_to_index2D(tuple(("b", 2))), white),
            Pawn  (tuple(("c", 2)), self.coord2D_to_index2D(tuple(("c", 2))), white),
            Pawn  (tuple(("d", 2)), self.coord2D_to_index2D(tuple(("d", 2))), white),
            Pawn  (tuple(("e", 2)), self.coord2D_to_index2D(tuple(("e", 2))), white),
            Pawn  (tuple(("f", 2)), self.coord2D_to_index2D(tuple(("f", 2))), white),
            Pawn  (tuple(("g", 2)), self.coord2D_to_index2D(tuple(("g", 2))), white),
            Pawn  (tuple(("h", 2)), self.coord2D_to_index2D(tuple(("h", 2))), white),
            Rook  (tuple(("a", 1)), self.coord2D_to_index2D(tuple(("a", 1))), white),
            Knight(tuple(("b", 1)), self.coord2D_to_index2D(tuple(("b", 1))), white),
            Bishop(tuple(("c", 1)), self.coord2D_to_index2D(tuple(("c", 1))), white),
            King  (tuple(("d", 1)), self.coord2D_to_index2D(tuple(("d", 1))), white),
            Queen (tuple(("e", 1)), self.coord2D_to_index2D(tuple(("e", 1))), white),
            Bishop(tuple(("f", 1)), self.coord2D_to_index2D(tuple(("f", 1))), white),
            Knight(tuple(("g", 1)), self.coord2D_to_index2D(tuple(("g", 1))), white),
            Rook  (tuple(("h", 1)), self.coord2D_to_index2D(tuple(("h", 1))), white)
        ]
        self.blackFigs = [
            Pawn  (tuple(("a", 7)), self.coord2D_to_index2D(tuple(("a", 7))), black),
            Pawn  (tuple(("b", 7)), self.coord2D_to_index2D(tuple(("b", 7))), black),
            Pawn  (tuple(("c", 7)), self.coord2D_to_index2D(tuple(("c", 7))), black),
            Pawn  (tuple(("d", 7)), self.coord2D_to_index2D(tuple(("d", 7))), black),
            Pawn  (tuple(("e", 7)), self.coord2D_to_index2D(tuple(("e", 7))), black),
            Pawn  (tuple(("f", 7)), self.coord2D_to_index2D(tuple(("f", 7))), black),
            Pawn  (tuple(("g", 7)), self.coord2D_to_index2D(tuple(("g", 7))), black),
            Pawn  (tuple(("h", 7)), self.coord2D_to_index2D(tuple(("h", 7))), black),
            Rook  (tuple(("a", 8)), self.coord2D_to_index2D(tuple(("a", 8))), black),
            Knight(tuple(("b", 8)), self.coord2D_to_index2D(tuple(("b", 8))), black),
            Bishop(tuple(("c", 8)), self.coord2D_to_index2D(tuple(("c", 8))), black),
            Queen (tuple(("d", 8)), self.coord2D_to_index2D(tuple(("d", 8))), black),
            King  (tuple(("e", 8)), self.coord2D_to_index2D(tuple(("e", 8))), black),
            Bishop(tuple(("f", 8)), self.coord2D_to_index2D(tuple(("f", 8))), black),
            Knight(tuple(("g", 8)), self.coord2D_to_index2D(tuple(("g", 8))), black),
            Rook  (tuple(("h", 8)), self.coord2D_to_index2D(tuple(("h", 8))), black),
        ]
        
        # Set / update tiles with figures on 
        for figColorGroup in list([self.whiteFigs, self.blackFigs]):
            for fig in figColorGroup:
                tile = self.board.getTileByCoord2D(fig.coord2D)
                if(tile is not None):
                    tile.update(fig.typee, fig.color)

        # DEV util
        # -----------------------------------
        # for row in self.board.tiles:
        #     for tile in row:
        #         tile.print()
        #     print()
        # -----------------------------------
    
    def coord2D_to_index2D(self, coord2D):        
        indexHor = self.board.letters_to_indexes07_Map.get(coord2D[0])
        indexVer = self.board.dim - coord2D[1]
        return tuple((indexHor, indexVer))
    
    def printBoard(self):
        
        # Graphics
        # -----------------------------------
        tileLength    = 11
        tileHeight    = 5
        
        whiteTileSym  = "#"
        blackTileSym  = "`"
        
        whiteFigSym   = "+"
        blackFigSym   = "\""
        
        emptySpaceSym = " "
        
        verFrameSym   = "@"
        horFrameSym   = "@"
        # -----------------------------------
        
        # Only odd numbers allowed
        # Minimum tile size = 5 (both dim)
        if(
           (tileLength % 2 == 1) and
           (tileHeight % 2 == 1) and
           (tileLength >= 5) and
           (tileHeight >= 5)
          ):
            
            # Top-horizontal bar
            # -----------------------------------
            for hor in range(self.board.dim):
                for length in range(tileLength):
                    print(horFrameSym, end = "")
            print(horFrameSym * 2, end = "\n")
            # -----------------------------------
            
            # Tiles and figures
            # -----------------------------------
            isTileEmpty = None
            tileColor   = None
            
            for ver in range(self.board.dim):
                for height in range(tileHeight):
                    
                    # Left-vertical bar
                    # -----------------------------------
                    print(verFrameSym, end = "")
                    # -----------------------------------
                    
                    for hor in range(self.board.dim):
                        for length in range(tileLength):
                            
                            # Guess if the tile is empty
                            if(self.board.tiles[ver][hor].figOn == None):
                                isTileEmpty = True
                            else:
                                isTileEmpty = False
                                
                            # Guess the tile color
                            #   if black then use blackTileSym
                            #   else use whiteTileSym
                            if(ver % 2 == 1):
                                if(hor % 2 == 1):
                                    tileColor = whiteTileSym
                                else:
                                    tileColor = blackTileSym
                            elif(ver % 2 == 0):
                                if(hor % 2 == 0):
                                    tileColor = whiteTileSym
                                else:
                                    tileColor = blackTileSym
                                    
                            # When in the center of the tile:
                            #   if no figure on the tile print tileColor
                            #   else print figure-ID
                            if(height == math.floor(tileHeight / 2) and length == math.floor(tileLength / 2)):
                                if(isTileEmpty == True):
                                    print(tileColor, end = "")
                                else:
                                    print(self.board.tiles[ver][hor].figOn, end = "")        
                            # When in 1-char distance from the center of the tile:
                            #   if no figure on the tile print tileColor
                            #   else print figSym
                            elif(
                                 (abs(height - math.floor(tileHeight / 2)) == 1 and abs(length - math.floor(tileLength / 2)) <= 1) or
                                 (abs(height - math.floor(tileHeight / 2)) <= 1 and abs(length - math.floor(tileLength / 2)) == 1)
                                ):
                                if(isTileEmpty == True):
                                    print(tileColor, end = "")
                                else:
                                    if(self.board.tiles[ver][hor].figColor == white):
                                        print(whiteFigSym, end = "")
                                    elif(self.board.tiles[ver][hor].figColor == black):
                                        print(blackFigSym, end = "")
                            # When painting the rest of the tile:
                            else:
                                print(tileColor, end = "")
                    
                    # Right-vertical bar
                    # -----------------------------------
                    print(verFrameSym, end = "\n")
                    # -----------------------------------
            # -----------------------------------
            
            # Bot-horizontal bar
            # -----------------------------------
            for hor in range(self.board.dim):
                for length in range(tileLength):
                    print(horFrameSym, end = "")
            print(horFrameSym * 2, end = "\n")
            # -----------------------------------
    
    def makeMove(self, move):
        figures = eval("self." + self.players.players[self.players.hasMove].color + "Figs")
        for figure in figures:

            # Check if current player has a figure at old_coord2D (move[0]) and if it's possible to move it to the new_coord2D (move[1])  
            if(figure.coord2D == move[0] and figure.makeMove(move[1], self.coord2D_to_index2D(move[1]))):
                
                # Update tile at new_coord2D
                new_index2D = self.coord2D_to_index2D(move[1])
                self.board.tiles[new_index2D[1]][new_index2D[0]].update(figure.typee, figure.color)

                # Update tile at old_coord2D
                old_index2D = self.coord2D_to_index2D(move[0])
                self.board.tiles[old_index2D[1]][old_index2D[0]].update(None, None)

                # For Pawn to know whether this is its first move
                figure.moved = True
                
                print("made move: with " + figure.color + " " + figure.typee + ", from " + str(move[0]) + ", to " + str(move[1]))

                # DEV util
                # -----------------------------------
                # for row in self.board.tiles:
                #     for tile in row:
                #         tile.print()
                #     print()
                # -----------------------------------

                return True
            
        print("can't make move")
        return False

    def startChess(self):
        
        # Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("make move:")
        
        # Valid-move-form flags
        isMoveFormLongEnough        = None
        isDelimeterColon            = None
        isNewPosDifferent           = None
        isFirstSymOldPosSmallLetter = None
        isFirstSymNewPosSmallLetter = None
        isSecondSymOldPosNumber     = None
        isSecondSymNewPosNumber     = None
        
        while(self.players.winner == None):
            self.printBoard()
            print(self.players.players[self.players.hasMove].color + " has turn.")
                    
            # Ask player to enter his move
            move = input("move: ")
                    
            # Clear terminal
            os.system('cls' if os.name == 'nt' else 'clear')
                    
            if(len(move) == 5):
                isMoveFormLongEnough = True

                if(move[2] == ":"):
                    isDelimeterColon = True
                else:
                    isDelimeterColon = False
                    print("delimeter must be a colon -> is " + move[2])

                if(move[0:2] != move[3:5]):
                    isNewPosDifferent = True
                else:
                    isNewPosDifferent = False
                    print("new position must be different from old one")

                if(move[0] in self.board.letters):
                    isFirstSymOldPosSmallLetter = True
                else:
                    isFirstSymOldPosSmallLetter = False
                    print("old position: letter must be in range a ~ h")

                if(move[3] in self.board.letters):
                    isFirstSymNewPosSmallLetter = True
                else:
                    isFirstSymNewPosSmallLetter = False
                    print("new position: letter must be in range a ~ h")

                if(int(move[1]) in self.board.indexes18):
                    isSecondSymOldPosNumber = True
                else:
                    isSecondSymOldPosNumber = False
                    print("old position: number must be in range 1 ~ 8")

                if(int(move[4]) in self.board.indexes18):
                    isSecondSymNewPosNumber = True
                else:
                    isSecondSymNewPosNumber = False
                    print("new position: number must be in range 1 ~ 8")
            else:
                isMoveFormLongEnough = False
                print("your move should be entered as \'a2:a3\' -> is " + move)

            # Check if "move" is a string like "a3:b3"
            # Check if move can be made
            if(
               isMoveFormLongEnough        and
               isDelimeterColon            and
               isNewPosDifferent           and
               isFirstSymOldPosSmallLetter and
               isFirstSymNewPosSmallLetter and
               isSecondSymOldPosNumber     and
               isSecondSymNewPosNumber
              ):
                old_index2D = tuple((move[0], int(move[1])))
                new_index2D = tuple((move[3], int(move[4])))
                tupled_move = tuple((old_index2D, new_index2D))
                if(self.makeMove(tupled_move)):
                    self.players.changeTurn()


game = Chess()
game.startChess()