import MsgType
import Board
import Side

class MoveTurn:
    def __init__(self):
       this.end = False
       this.again = False
       this.move =  0

class Protocol:
    @staticmethod
    def createMoveMsg(hole):
        return "MOVE;" + hole + "\n"

    @staticmethod
    def createSwapMsg():
        return "SWAP\n"

    @staticmethod
    def getMessageType(msg):
        if (msg.startswith("START;")):
            return MsgType.START
        elif (msg.startsWith("CHANGE;")):
            return MsgType.STATE
        elif (msg.equals("END\n")):
            return MsgType.END
        else:
            raise Exception("Could not determine message type.")

    @staticmethod
    def interpretStartMsg(msg):
        if (msg[-1] != "\n"):
            raise Exception("Message not terminated with 0x0A character.")

        position = msg[6:(len(msg) - 1)]
        if (position == "South"):
            return True
        elif(position == "North"):
            return False
        else:
            raise Exception("Illegal position parameter: " + position)

    @staticmethod
    def interpretStateMsg(msg, board):
        moveTurn = MoveTurn()

        if (msg[-1] != "\n"):
            raise Exception("Message not terminated with 0x0A character.")

        msgParts = msg.split(";", 4)
        if (len(msgParts) != 4):
            raise Exception("Missing arguments.")

        if (msgParts[1] == "SWAP"):
            moveTurn.move = -1
        else:
            moveTurn.move = int(msgParts[1])
        
        boardParts = msgParts[2].split(",", -1)
        if (2 * (board.getNoOfHoles() + 1) != len(boardParts)):
            raise Exception("Board dimensions in message (" + len(boardParts) + " entries) are not as expected (" + 2 * (board.getNoOfHoles() + 1) + " entries).")

        for i in range(board.getNoOfHoles()):
            board.setSeeds(Side.NORTH, i + 1, int(boardParts[i]))
        board.setSeedsInStore(Side.NORTH, int(boardParts[board.getNoOfHoles()]))
        for i in range(board.getNoOfHoles()):
            board.setSeeds(Side.SOUTH, i + 1, int(boardParts[i+board.getNoOfHoles()+1]))
        board.setSeedsInStore(Side.SOUTH, int(boardParts[2 * board.getNoOfHoles() + 1]))

        moveTurn.end = False
        if (msgParts[3] == "YOU\n"):
            moveTurn.again = True
        elif (msgParts[3] == "OPP\n"):
            moveTurn.again = False
        elif (msgParts[3] == "END\n"):
            moveTurn.end = True
            moveTurn.again  = False
        else:
            raise Exception("Illegal value for turn parameter: " + msgParts[3])

        return moveTurn