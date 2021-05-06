import numpy as np
from Game.Side import Side

class Board:
    NORTH_ROW = 0
    SOUTH_ROW = 1
    
    def __init__(self, holes, seeds):
        if (holes < 1):
            raise Exception("There has to be at least one hole, but " + holes + " were requested.")
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
            
        self.holes = holes
        self.seeds = seeds
        self.board = np.zeros(shape = (2, holes + 1), dtype=int)
        
        for i in range(1, holes + 1):
            self.board[Board.NORTH_ROW][i] = seeds
            self.board[Board.SOUTH_ROW][i] = seeds

    @staticmethod
    def indexOfSide(side):
        if side == Side.NORTH:
            return Board.NORTH_ROW
        elif side == Side.SOUTH:
            return Board.SOUTH_ROW
        else:
            return -1
    
    def clone(self):
        newBoard = Board(self.holes, self.seeds)
        newBoard.board = np.copy(self.board)
        return newBoard
    
    def getNoOfHoles(self):
        return self.holes

    def getSeeds(self, side, hole):
        if (hole < 1 or hole > self.holes):
            raise Exception(f"Hole number must be between 1 and {len(self.board[Board.NORTH_ROW]) - 1} but was {hole}.")
        return self.board[Board.indexOfSide(side)][hole]
    
    def setSeeds(self, side, hole, seeds):
        if (hole < 1 or hole > self.holes):
            raise Exception(f"Hole number must be between 1 and {len(self.board[Board.NORTH_ROW]) - 1} but was {hole}.")
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
        
        self.board[Board.indexOfSide(side)][hole] = seeds
        
    def addSeeds(self, side, hole, seeds):
        if (hole < 1 or hole > self.holes):
            raise Exception(f"Hole number must be between 1 and {len(self.board[Board.NORTH_ROW]) - 1} but was {hole}.")
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
        
        self.board[Board.indexOfSide(side)][hole] += seeds
        
    def getSeedsOp(self, side, hole):
        if (hole < 1 or hole > self.holes):
            raise Exception(f"Hole number must be between 1 and {len(self.board[Board.NORTH_ROW]) - 1} but was {hole}.")
        
        return self.board[1 - Board.indexOfSide(side)][self.holes + 1 - hole]
    
    def setSeedsOp(self, side, hole, seeds):
        if (hole < 1 or hole > self.holes):
            raise Exception(f"Hole number must be between 1 and {len(self.board[Board.NORTH_ROW]) - 1} but was {hole}.")
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
        
        self.board[1 - Board.indexOfSide(side)][self.holes + 1 - hole] = seeds
    
    def addSeedsOp(self, side, hole, seeds):
        if (hole < 1 or hole > self.holes):
            raise Exception(f"Hole number must be between 1 and {len(self.board[Board.NORTH_ROW]) - 1} but was {hole}.")
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
        
        self.board[1 - Board.indexOfSide(side)][self.holes + 1 - hole] += seeds
        
    def getSeedsInStore(self, side):
        return self.board[Board.indexOfSide(side)][0]
    
    def setSeedsInStore(self, side, seeds):
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
        
        self.board[Board.indexOfSide(side)][0] = seeds
        
    def addSeedsToStore(self, side, seeds):
        if (seeds < 0):
            raise Exception("There has to be a non-negative number of seeds, but " + seeds + " were requested.")
        
        self.board[Board.indexOfSide(side)][0] += seeds
    
   # def toString(self):
      #  boardString = ""
      #  boardString.append(self.board[Board.NORTH_ROW][0] + "  --")
      #  for i in range(self.holes, 0, -1):
       #     boardString.append("  " + self.board[Board.NORTH_ROW][i])
       # boardString.append("\n")
      #  for i in range(1, self.holes + 1):
     #       boardString.append(self.board[Board.SOUTH_ROW][i] + "  ")
     #   boardString.append("--  " + self.board[Board.SOUTH_ROW][0] + "\n")
        
      #  return boardString

    def __str__(self):
        boardString = ""
        boardString = boardString + str(self.board[Board.NORTH_ROW][0]) +" --"
        for i in range(self.holes, 0, -1):
            boardString = boardString + "  " + str(self.board[Board.NORTH_ROW][i])
        boardString = boardString + ("\n")
        for i in range(1, self.holes + 1):
            boardString = boardString +str(self.board[Board.SOUTH_ROW][i]) + " " 
        boardString = boardString + "-- "+str( self.board[Board.SOUTH_ROW][0]) + "\n"
        
        return boardString
    def __eq__(self, other): 
        if not isinstance(other, Board):
            # don't attempt to compare against unrelated types
            return NotImplemented
        else:
            return self.holes == other.holes and self.seeds == other.seeds \
                   and self.board == other.board
