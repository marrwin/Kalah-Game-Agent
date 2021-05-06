from Game.Board import *
from Game.Game import *
from Game.Move import *
from Game.Side import *
from MKAgent.Agent import *
from MKAgent.RandomAgent import *

NUMBER_EPESOIDS = 100000
agent1Wins = 0
agent1South = 0
agent1North = 0
agent2Wins = 0
agent2South = 0
agent2North = 0
draw = 0

agent1 = RandomAgent()
agent2 = RandomAgent()
moves = []

# Show progress bar if library is installed
# To install progress bar run this command: pip install tqdm
iterable = None
try:
    from tqdm import tqdm
    iterable = tqdm(range(NUMBER_EPESOIDS))
except:
    iterable = range(NUMBER_EPESOIDS)

for noGames in iterable:
    currentGame = Game(Board(7, 7), agent1, agent2)
    currentPair = currentGame.play()
    moves.append(currentPair)
    if (currentPair[1] == None):
        draw += 1
    else:
        if (currentPair[1] == agent1.getSide()):
            agent1Wins += 1
            if (agent1.getSide() == Side.SOUTH):
                agent1South += 1
            else:
                agent1North += 1
        elif(currentPair[1] == agent2.getSide()):
            agent2Wins += 1
            if (agent2.getSide() == Side.SOUTH):
                agent2South += 1
            else:
                agent2North += 1

print(f"\nagent1 wins: {agent1Wins}; South: {agent1South}; North: {agent1North}")
print(f"agent2 wins: {agent2Wins}; South: {agent2South}; North: {agent2North}")
print(f"draws: {draw}")

