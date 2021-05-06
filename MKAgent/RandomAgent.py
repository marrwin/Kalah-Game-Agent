import numpy as np

from MKAgent.Agent import Agent
from Game.Move import Move

class RandomAgent(Agent):
    def __init__(self):
        super().__init__()

    def play(self, board, firstGame):
        if (self.side != None):
            options = self.getNextValidOptions(board, firstGame)
            if (len(options) > 0):
                return options[np.random.randint(len(options))]
            else:
                return Move(self.side, 1)
        raise Exception("Can't start the game without setting the sides of the game!")