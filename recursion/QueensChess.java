package recursion;

import java.util.Arrays;

public class QueensChess {

    public static void main(String[] args) {
    	int[][] in1 = new int[3][3];  //default to 0s
		placeQueens(in1, 2, 0, 0);
   	}

    public static void placeQueens(int[][] board, int queens, int row, int col) {
        if (queens == 0) {
            printArray(board);
        } else if (!spotOnBoard(board, row, col)) {
	    //do nothing
	} else if (spotEligible(board, row, col) ) {
	    System.out.println("spot is not eligible");
	    board[row][col] = 1;
	    placeQueens(board, queens-1, row+1, col);
	    board[row][col] = 0;
	    placeQueens(board, queens, row, col+1);
	    //do nothing
	} else {
	    placeQueens(board, queens, row, col+1);
	    placeQueens(board, queens, row+1, col);
	    //placeQueens(board, queens-1, row-1, col-1);
        }
    }

    private static boolean spotOnBoard(int[][] board, int row, int col) {
        if (row < 0 || row >= board.length) {
            return false;
        } else if (col < 0 || col >= board[0].length) {
            return false;
        } else {
            return true;
        }
    }

    private static boolean spotEligible(int[][] board, int row, int col) {
        for (int i=0; i<board.length; i++) {
            if (board[i][col] == 1) {
                return false;
            }
        }
        for (int j=0; j<board[0].length; j++) {
            if (board[row][j] == 1) {
                return false;
            }
        }
        return true;
    }

    private static void printArray(int[][] arr) {
        System.out.println("_________");
        for (int i=0; i<arr.length; i++) {
            System.out.println(Arrays.toString(arr[i]));
        }
    }



}
