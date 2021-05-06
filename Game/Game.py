import numpy as np

from Game.Side import *
from Game.Kalah import *
from Game.Move import *

class Game:
    def __init__(self, board, agent1, agent2):
        self.kalah = Kalah(board)
        
        self.moves = []
        if (np.random.randint(2) == 0):
            agent1.setSide(Side.SOUTH)
            self.south = agent1
            agent2.setSide(Side.NORTH)
            self.north = agent2
        else:
            agent1.setSide(Side.NORTH)
            self.north = agent1
            agent2.setSide(Side.SOUTH)
            self.south = agent2
        
    def getMoves(self):
        return self.moves
    
    def getBoard(self):
        return self.kalah.getBoard()
    
    @staticmethod
    def getWinnerStatic(board):
        totalSouth = board.getSeedsInStore(Side.SOUTH)
        totalNorth = board.getSeedsInStore(Side.NORTH)
        
        if (totalSouth > totalNorth):
            return Side.SOUTH
        elif (totalSouth < totalNorth):
            return Side.NORTH
        else:
            return None
    
    def play(self):
        currentMove = self.south.play(self.kalah.getBoard(), True)
        self.moves.append(currentMove)
        currentSide = self.kalah.makeMove(currentMove);
        
        if (not self.kalah.gameOver()):
            currentMove = self.north.play(self.kalah.getBoard(), True)
            self.moves.append(currentMove)
            
            if (currentMove.getHole() < 0):
                temp = self.south
                self.south = self.north
                self.south.setSide(Side.SOUTH)
                self.north = temp
                self.north.setSide(Side.NORTH)
            else:
                currentSide = self.kalah.makeMove(currentMove)
                
            while(not self.kalah.gameOver()):
                if currentSide == Side.SOUTH:
                    currentMove = self.south.play(self.kalah.getBoard(), False)
                    self.moves.append(currentMove)
                    currentSide = self.kalah.makeMove(currentMove)
                else:
                    currentMove = self.north.play(self.kalah.getBoard(), False)
                    self.moves.append(currentMove)
                    currentSide = self.kalah.makeMove(currentMove)
        
        winner = Game.getWinnerStatic(self.kalah.getBoard());
        return (self.moves, winner)