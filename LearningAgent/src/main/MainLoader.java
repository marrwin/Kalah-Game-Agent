package main;
import java.util.ArrayList;
import java.util.List;

import Game.Board;
import Game.Game;
import Game.Move;
import Game.Side;
import Helper.Pair;
import MKAgent.Agent;
import MKAgent.RandomAgent;

/**
 * The main application class. It also provides methods for communication with
 * the game engine.
 */
public class MainLoader {
	private final static int NUMBER_EPESOIDS = 10000;
	private static List<Pair<Move[], Side>> moves;
	//stats value
	private static int agent1Wins = 0;
	private static int agent1South = 0;
	private static int agent1North = 0;
	private static int agent2Wins = 0;
	private static int agent2South = 0;
	private static int agent2North = 0;
	private static int draw = 0;

	/**
	 * The main method, invoked when the program is started.
	 * 
	 * @param args Command line arguments.
	 */
	public static void main(String[] args) {
		Agent agent1 = new RandomAgent();
		Agent agent2 = new RandomAgent();
		moves = new ArrayList<Pair<Move[], Side>>();
		for (int noGames = 0; noGames < NUMBER_EPESOIDS; noGames++) {
			Game currentGame = new Game(new Board(7, 7), agent1, agent2);
			Pair<Move[], Side> currentPair = currentGame.Play();
			moves.add(currentPair);
			if (currentPair.getElement2() == null) {
				draw++;
			} else {
				if (currentPair.getElement2().equals(agent1.getSide())) {
					agent1Wins++;
					if(agent1.getSide().equals(Side.SOUTH)) {
						agent1South++;
					}else {
						agent1North++;
					}
				} else if (currentPair.getElement2().equals(agent2.getSide())) {
					agent2Wins++;
					if(currentPair.getElement2().equals(Side.SOUTH)) {
						agent2South++;
					}else {
						agent2North++;
					}
				}
			}
			
			
		}

		printResults();

	}

	private static void printResults() {
		System.out.println("agent1 wins: " + agent1Wins + "; South: " + agent1South + "; North: " + agent1North);
		System.out.println("agent2 wins: " + agent2Wins + "; South: " + agent2South + "; North: " + agent2North);
		System.out.println("draws: " + draw);
	}
}
