package Game;

import java.util.ArrayList;
import java.util.List;

import Helper.Pair;
import Helper.Random;
import MKAgent.Agent;

public class Game {
	private Agent south;
	private Agent north;
	private Kalah kalah;
	private List<Move> moves;

	public Game(Board board, Agent agent1, Agent agent2) {
		this.kalah = new Kalah(board);

		moves = new ArrayList<Move>();
		if (Random.getRandomNumber(0, 2) == 0) {

			agent1.setSide(Side.SOUTH);
			this.south = agent1;
			agent2.setSide(Side.NORTH);
			this.north = agent2;
		} else {
			agent1.setSide(Side.NORTH);
			this.north = agent1;
			agent2.setSide(Side.SOUTH);
			this.south = agent2;

		}
	}

	public List<Move> getMoves() {
		return moves;
	}

	public Board getBoard() {
		return this.kalah.getBoard();
	}

	// method used to perform a full game and reports back list of moves performed
	// by
	// sides
	public Pair<Move[], Side> Play() {
		Move currentMove;

		// first the south make first move
		currentMove = south.play(kalah.getBoard(),true);
		// store move in array
		moves.add(currentMove);
		// apply move to kalah and update currentSide
		Side currentSide = kalah.makeMove(currentMove);
		
		
		// System.out.println(currentSide);
		if (!kalah.gameOver()) {

			// secound player make move
			currentMove = north.play(kalah.getBoard(),true);
			// store move in array
			moves.add(currentMove);

			// if move is swap:
			if (currentMove.getHole() < 0) {
				// swap players and update currentSide
				Agent temp = south;
				south = north;
				south.setSide(Side.SOUTH);
				north = temp;
				north.setSide(Side.NORTH);
			}
			else {
				// apply move to kalah and update currentSide
				currentSide = kalah.makeMove(currentMove);
			}
			// while the game not over
			while (!kalah.gameOver()) {
				// switch currentSide:
				switch (currentSide) {			
				// player 1 move:
				case SOUTH:
					// get player 1 move
					currentMove = south.play(kalah.getBoard(),false);
					//System.out.println(currentMove);
					// store move in array
					moves.add(currentMove);
					// apply move to kalah and update currentSide
					currentSide = kalah.makeMove(currentMove);
					// System.out.println(currentSide);

					// player 2 move:
					break;
				case NORTH:
					// get player 2 move
					currentMove = north.play(kalah.getBoard(),false);
					//System.out.println(currentMove);
					// store move in array
					moves.add(currentMove);
					// apply move to kalah and update currentSide
					currentSide = kalah.makeMove(currentMove);
					// System.out.println(currentSide);

				}
				 //System.out.println(currentMove);

			}
		}
		Side winner = getWinner(kalah.getBoard());
		//System.out.println(winner);
		return new Pair<Move[], Side>(moves.toArray(new Move[0]), winner);
	}

	private Side getWinner(Board board) {
		int totalSouth = board.getSeedsInStore(Side.SOUTH);
		int totalNorth = board.getSeedsInStore(Side.NORTH);

		if (totalSouth > totalNorth)
			return Side.SOUTH;
		else if (totalSouth < totalNorth)
			return Side.NORTH;
		else
			return null;

	}

}