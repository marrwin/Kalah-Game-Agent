from MKAgent.Agent import Agent
from DQNAgent.Model import Model
from Game.Side import Side
from Game.Move import Move

class DQNAgent(Agent):
    def __init__(self, model, alwaysExploite=False):
        super().__init__()
        self.model = model
        self.alwaysExploite = alwaysExploite
        
    def play(self, board, firstGame):
        if (self.side == None):
            raise Exception("Can't start the game without setting the sides of the game!")
            
        if (firstGame and self.side == Side.NORTH):
            # Always switch
            return Move(self.side, -1)
        action = self.model.act(Model.boardToStateStatic(self.side, board), self.alwaysExploite)

        return Move(self.side, action)