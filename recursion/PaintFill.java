package recursion;

import java.util.Arrays;

public class PaintFill {
    
    public static int[][] in1 = new int[3][3];
    public static int[][] in2 = {
	{ 0, 1, 1 },
	{ 1, 0, 0 },
	{ 1, 0, 0 }
    };

    public static void main(String[] args) {
	//boolean[][] in1 = new boolean[3][3];
        int[][] out1 = {
	    { 1, 1, 1 },
	    { 1, 1, 1 },
	    { 1, 1, 1 }
	};
	fillPaint(in1, 1,1);
	for (int i=0; i<in1.length; i++) {
	    System.out.println(Arrays.equals(out1[i],in1[i]));
	    //System.out.println(Arrays.toString(row));
	}

        int[][] out2 = {
	    { 0, 1, 1 },
	    { 1, 1, 1 },
	    { 1, 1, 1 }
	};
	fillPaint(in2,2,2);
	for (int i=0; i<in2.length; i++) {
	    System.out.println(Arrays.equals(out2[i],in2[i]));
	    //System.out.println(Arrays.toString(row));
	}
    }


    public static void fillPaint(int[][] matrix, int row, int col) {
	matrix[row][col] = 1;

	//left
	if (col-1 >= 0 && matrix[row][col-1] != 1) {
	    fillPaint(matrix, row, col-1);
	}
	//right
	if (col+1 < matrix[0].length && matrix[row][col+1] != 1) {
	    fillPaint(matrix, row, col+1);
	}
	//down
	if (row+1 < matrix.length && matrix[row+1][col] != 1) {
	    fillPaint(matrix, row+1, col);
	}
	//up
	if (row-1 >= 0 && matrix[row-1][col] != 1) {
	    fillPaint(matrix, row-1, col);
	}
    }
    
}
