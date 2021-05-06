package MKAgent;

import java.util.ArrayList;
import java.util.List;

import Game.Board;
import Game.Kalah;
import Game.Move;
import Game.Side;

public abstract class Agent {
	// which side the player (south or north)
	protected Side side;

	public abstract Move play(Board board, boolean firstGame);


	protected List<Move> getNextValidOptions(Board board, boolean firstGame) {
		// list to store all valid moves
		List<Move> moves = new ArrayList<Move>();
		// create new kala
		for (int index = 1; index <= board.getNoOfHoles(); index++) {
			Move currentMove = new Move(side, index);
			if (Kalah.isLegalMove(board, currentMove)) {
				moves.add(currentMove);
			}
		}
		if (firstGame && side.equals(Side.NORTH))
			moves.add(new Move(side, -1));
		return moves;
	}

	public void setSide(Side side) {
		this.side = side;
	}

	public Side getSide() {
		return this.side;
	}
	
	private static Side getWinner(Board board) {
		int totalSouth = board.getSeedsInStore(Side.SOUTH);
		int totalNorth = board.getSeedsInStore(Side.NORTH);

		if (totalSouth > totalNorth)
			return Side.SOUTH;
		else if (totalSouth < totalNorth)
			return Side.NORTH;
		else
			return null;

	}
	
	/**
	 * 
	 * @param lastBoard: the board state before move
	 * @param currentBoard: the board state after move
	 * @param side: Agent's side
	 * @param secondTurn: if Agent has a second turn
	 * @return
	 */
	public static Integer getReward(Board lastBoard, Board currentBoard, Side side, Boolean secondTurn) {
		
		int reward = 0;
		
		reward = ((currentBoard.getSeedsInStore(side) - lastBoard.getSeedsInStore(side)) * 10) +
					((currentBoard.getSeedsInStore(side.opposite()) - lastBoard.getSeedsInStore(side.opposite())) * -10);
		
		if (getWinner(currentBoard) == side) {
			reward += 100;
		}
		
		if (secondTurn) {
			reward += 20;
		}
		
		return reward;
	}

}