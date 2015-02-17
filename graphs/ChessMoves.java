package graphs;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;

public class ChessMoves {
    
    private static final int[][] KNIGHT_MOVES = { {2,1},
					   {2,-1},
					   {-2,1},
					   {-2,-1},
					   {1,2},
					   {1,-2},
					   {-1,2},
					   {-1,-2} };
    private static final int[][] KING_MOVES = { {1,1},
					 {1,-1},
					 {1,0},
					 {-1,1},
					 {-1,-1},
					 {-1,0},
					 {0,1},
					 {0,-1} };

    public static void main(String[] args) {
	ChessMoves chess = new ChessMoves();
	//Knight
	System.out.println(chess.getMinMoves(3,3,1,4,KNIGHT_MOVES) == 1);
	System.out.println(chess.getMinMoves(3,3,3,3,KNIGHT_MOVES) == 0);
	System.out.println(chess.getMinMoves(3,3,2,6,KNIGHT_MOVES) == 2);
	System.out.println(chess.getMinMoves(0,0,1,3,KNIGHT_MOVES) == 2);

	//King
	System.out.println(chess.getMinMoves(3,3,1,4,KING_MOVES) == 2);
	System.out.println(chess.getMinMoves(3,3,3,3,KING_MOVES) == 0);
	System.out.println(chess.getMinMoves(3,3,2,6,KING_MOVES) == 3);
	System.out.println(chess.getMinMoves(0,0,1,3,KING_MOVES) == 3);
    }

    private class Square {
	public int x;
	public int y;
	public int distance; //defaults to 0

	public Square(int x, int y) {
	    this.x = x;
	    this.y = y;
	}
    }

    public int getMinMoves(int x1, int y1, int x2, int y2, int[][] possibleMoves) {
	List<Square> visited = new ArrayList();
	Queue<Square> queue = new LinkedList();
	Square square = new Square(x1,y1);
	queue.add(square);
	while(queue.peek() != null) {
	    square = queue.remove();
	    if (square.x == x2 && square.y == y2) {
		return square.distance;
	    } else {
		List<Square> children = getEligibleMoves(square, possibleMoves);
		for (Square child : children) {
		    if (!visited(child, visited)) {
			child.distance = square.distance + 1;
			queue.add(child);
		    }
		}		
	    }
	    visited.add(square);
	}
	return -1;
    }

    private List<Square> getEligibleMoves(Square square, int[][] possibleMoves) {
	List<Square> eligibleMoves = new ArrayList();
	for (int[] move : possibleMoves) {
	    int posX = square.x + move[0];
	    int posY = square.y + move[1];
	    if (posX >= 0 && posX <= 9 && posY >= 0 && posY <= 9) {
		Square newSquare = new Square(posX,posY);
		eligibleMoves.add(newSquare);
	    }
	}
	return eligibleMoves;
    }

    private boolean visited(Square target, List<Square> visitedSquares) {
	for (Square square: visitedSquares) {
	    if (target.x == square.x && target.y == square.y) {
		return true;
	    }
	}
	return false;
    }

}
