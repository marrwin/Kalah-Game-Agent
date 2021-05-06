package MKAgent;

import java.util.ArrayList;
import java.util.List;

import Game.Board;
import Game.Kalah;
import Game.Move;
import Game.Side;


public class Heuristics {
	
	// objective is to maximise difference
	public Integer howFarAhead(Board board, Side side) {
		
		int seedsInStore = board.getSeedsInStore(side);
		int seedsInOppositeStore = 	board.getSeedsInStore(side.opposite());
		
		int difference = seedsInStore - seedsInOppositeStore;
		return difference;
	}
	
	
	public Integer howCloseIAmToWinning(Board board, Side side) {
		
		int seedsInStore = board.getSeedsInStore(side);
		int difference = 49 - seedsInStore;
		
		return -(difference);
	}
	
	
	public Integer howCloseOpponentIsToWinning(Board board, Side side) {
		
		int seedsInStore = board.getSeedsInStore(side.opposite());
		int difference = 49 - seedsInStore;
		
		return difference;
	}
	
	
	public Integer numberOfSeedsCloseToMyHome(Board board, Side side) {
		
		int seeds = 0;
		for (int index = 1; index <= board.getNoOfHoles(); index++) {
			seeds += board.getSeeds(side, index);
		}
		
		return seeds;
	}
}
