import java.util.Arrays;
//import org.apache.commons.lang3.ArrayUtils;

public class SetMatrixToZero {

    public static void main(String[] args) {
    	int[][] in1 = {
		  { 0, 2, 3 },
		  { 4, 5, 6 },
		  { 7, 8, 4 }
		};
    	int[][] out1 = {
		  { 0, 0, 0 },
		  { 0, 5, 6 },
		  { 0, 8, 4 }
		};
		in1 = setMatrixToZero(in1);
		for (int i=0; i<in1.length; i++) {
			System.out.println(Arrays.equals(in1[i],out1[i]));
			//System.out.println(Arrays.toString(row));
		}
   	}

   	public static int[][] setMatrixToZero(int[][] matrix) {
   		int rowLen = matrix.length;
   		int colLen = matrix[0].length;
   		boolean[] rows = new boolean[rowLen];
   		boolean[] cols = new boolean[colLen];

   		for (int i=0; i<rowLen; i++) {
   			
   			for (int j=0; j<colLen; j++) {			
   				if (matrix[i][j] == 0) {
   					rows[i] = true;
   					cols[j] = true;
   				}
   			}
   		}

   		return setZeros(matrix, rows, cols);
   	}

   	private static int[][] setZeros(int[][] matrix, boolean[] rows, boolean[] cols) {
   		for (int i=0; i<matrix.length; i++) {
   			for (int j=0; j<matrix[i].length; j++) {
   				if (rows[i] || cols[j]) {
   					matrix[i][j] = 0;
   				}
   			}
   		}

   		return matrix;
   	}

}
