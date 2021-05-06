import plaidml.keras
import os
plaidml.keras.install_backend()
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import numpy as np
from MKAgent.RandomAgent import RandomAgent
from DQNAgent.RLAgent import DQNAgent
from DQNAgent.DQNGame import DQNGame
from DQNAgent.Model import Model
from Game.Board import Board
from Game.Side import Side

def getReward(currentBoard, nextBoard, playingSide, didResultInPlayingAgain, winningSide):
    WINNING = 100
    DRAW = -50
    SCORING = 10
    PLAY_AGAIN = 20
    
    if (nextBoard == None):
        if (winningSide == playingSide):
            return WINNING
        elif (winningSide == playingSide.opposite()):
            return -WINNING
        else:
            return DRAW
    
    reward = (((nextBoard.getSeedsInStore(playingSide) 
                    - currentBoard.getSeedsInStore(playingSide)) * SCORING) 
                +  ((nextBoard.getSeedsInStore(playingSide.opposite())  
                    - currentBoard.getSeedsInStore(playingSide.opposite())) * -SCORING))
    
    if didResultInPlayingAgain:
        reward += PLAY_AGAIN
        
    return reward

def getStateActionNextStateReward(boards, moves, winningSide):
    boardMoves = list(zip(boards, moves))
    boardMoves.append((None, None))
    
    memory = []
    for index, (board, move) in enumerate(boardMoves[:-1]):
        currentBoard = board
        if (boardMoves[index + 1][0] == None):
            playedAgain = False
        else:
            playedAgain = move.getSide() == boardMoves[index + 1][1].getSide()
            
        if (playedAgain):
            nextBoard = boardMoves[index + 1][0]
        else:
            nextBoard = next((boardMove for boardMove in boardMoves[(index + 1):-1] if boardMove[1].getSide() == move.getSide()), None)
            if (nextBoard != None):
                nextBoard = nextBoard[0]
        
        reward = getReward(currentBoard, nextBoard, move.getSide(), playedAgain, winningSide)
        done = (nextBoard == None)
        
        currentState = Model.boardToStateStatic(move.getSide(), currentBoard)
        action = move.getHole()
        
        nextState = None
        if (nextBoard != None):
            nextState = Model.boardToStateStatic(move.getSide(), nextBoard)
            
        memory.append((currentState, action, reward, nextState, done))
    
    return memory

def benchmarkAgainstRandomPlayer(model):
    dqnWin = 0
    randomWin = 0
    draw = 0
    model.resetIllegalMoves()

    for gameNumber in range(100):
        dqnAgent = DQNAgent(model, True)
        randomAgent = RandomAgent()
        game = DQNGame(Board(7,7), dqnAgent, randomAgent)
        moves, boards, winningSide = game.play()
        
        if (winningSide == None):
            draw += 1
        elif(winningSide == dqnAgent.getSide()):
            dqnWin += 1
        else:
            randomWin +=1
    
    print(f"DQN Won {dqnWin/100}, Random Won {randomWin/100}, Draw Rate: {draw/100}, Illegal Moves: {model.illegalMoves}")

def main():
    # 920 Game for epsilon to decay to min
    numberOfGames = 1000000
    iterable = None
    try:
        from tqdm import trange
        iterable = trange(numberOfGames)
    except:
        iterable = range(numberOfGames)

    outputDir = 'DQNAgent/model_output/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    model = Model()

    agent1 = DQNAgent(model)
    agent2 = DQNAgent(model)
    for gameNumber in iterable:
        game = DQNGame(Board(7,7), agent1, agent2)
        moves, boards, winningSide = game.play()
        
        # extract state, move, nextState, done
        memory = getStateActionNextStateReward(boards, moves, winningSide)
        model.rememeber(memory)

        if (len(model.memory) > model.batchSize):
            model.replay()

        if gameNumber % 50 == 0:
            print("weights_" + '{:04d}:'.format(gameNumber), end="")
            benchmarkAgainstRandomPlayer(model)
            print()

            model.save(outputDir + "weights_" + '{:04d}'.format(gameNumber) + ".hdf5")
            
if __name__ == "__main__":
    main()