import numpy as np

from Game.Side import *
from Game.Kalah import *
from DQNAgent.RLAgent import DQNAgent

class DQNGame:
    def __init__(self, board, agent1, agent2):
        self.kalah = Kalah(board)
    
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
    
    def getBoard(self):
        return self.kalah.getBoard()
    
    def getCopyBoard(self):
        return self.getBoard().clone()
    
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
    
    @staticmethod
    def checkIfWonStatic(board):
        totalSouth = board.getSeedsInStore(Side.SOUTH)
        if (totalSouth > 49):
            return True
    
        totalNorth = board.getSeedsInStore(Side.NORTH)
        if (totalNorth > 49):
            return True
        
        return False

    
    def play(self):
        moves = []
        boards = []
        
        # South Plays first Salim's Rule
        #currentSide = Side.SOUTH
        currentMove = self.south.play(self.getBoard(), True)
        moves.append(currentMove)
        boards.append(self.getCopyBoard())
        
        '''
        if (not Kalah.isLegalMoveStatic(self.getBoard(), currentMove)):
            return (moves, boards, currentSide.opposite())
        '''
        currentSide = self.kalah.makeMove(currentMove);
        
        #print(currentMove)
        #print(self.getCopyBoard())

        currentMove = self.north.play(self.getBoard(), True)
        moves.append(currentMove)
        boards.append(self.getCopyBoard())
        
        if (currentMove.getHole() < 0):
            self.kalah.board.board = np.flip(self.getBoard().board, 0)
            currentSide = Side.SOUTH
        else:
            '''
            if (not Kalah.isLegalMoveStatic(self.getBoard(), currentMove)):
                return (moves, boards, currentSide.opposite())
            '''
            currentSide = self.kalah.makeMove(currentMove)
       # print(currentMove)
        #print(self.getCopyBoard())
        while(not self.kalah.gameOver()):
            if (DQNGame.checkIfWonStatic(self.getBoard())):
                winningSide = DQNGame.getWinnerStatic(self.kalah.board);
                return (moves, boards, winningSide)
            if currentSide == Side.SOUTH:
                currentMove = self.south.play(self.getBoard(), False)
                moves.append(currentMove)
                boards.append(self.getCopyBoard())
                if (not Kalah.isLegalMoveStatic(self.getBoard(), currentMove)):
                    print("\n\nIllegal Move Played")
                    print(self.getBoard().board)
                    print(f"Hole Chosen: {currentMove.getHole()}, by Side: {currentMove.getSide()}")
                    if (type(self.south) == DQNAgent):
                        print("By DQN Agent\n\n")
                    else:
                        print("By Random Agent\n\n")

                    return (moves, boards, currentSide.opposite())
                currentSide = self.kalah.makeMove(currentMove)
            else:
                currentMove = self.north.play(self.getBoard(), False)
                moves.append(currentMove)
                boards.append(self.getCopyBoard())
                if (not Kalah.isLegalMoveStatic(self.getBoard(), currentMove)):
                    print("\n\nIllegal Move Played")
                    print(self.getBoard().board)
                    print(f"Hole Chosen: {currentMove.getHole()}, by Side: {currentMove.getSide()}")
                    if (type(self.south) == DQNAgent):
                        print("By DQN Agent\n\n")
                    else:
                        print("By Random Agent\n\n")
        
                    return (moves, boards, currentSide.opposite())
                currentSide = self.kalah.makeMove(currentMove)
          #  print(currentMove)
           # print(self.getCopyBoard())
        winningSide = DQNGame.getWinnerStatic(self.kalah.board);
        return (moves, boards, winningSide)