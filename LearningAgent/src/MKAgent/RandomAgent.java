package MKAgent;

import java.util.ArrayList;
import java.util.List;

import Game.Board;
import Game.Kalah;
import Game.Move;
import Game.Side;
import Helper.Random;

public class RandomAgent extends Agent {

	@Override
	public Move play(Board board, boolean firstGame) {
		if (side != null) {
			List<Move> options = getNextValidOptions(board, firstGame);
			if (options.size() > 0) {
				Move move = options.get(Random.getRandomNumber(0, options.size()));
				return move;
			} else
				return new Move(side, 1);
		}
		throw new IllegalCallerException("cant start the game without setting the sides of the game!");
	}


}