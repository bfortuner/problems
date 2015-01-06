package recursion;
import java.util.ArrayList;
import java.util.List;


public class RobotSquares {

    public static List<Integer[]> offLimitsArr = new ArrayList<Integer[]>();
    
    public static void main(String[] args) {
	int paths = getPossiblePaths(3,0,0);
	System.out.println(paths);
	Integer[] a1 = new Integer[2];
	a1[0] = 2;
	a1[1] = 2;
	offLimitsArr.add(a1);


	System.out.println(getPossiblePathsOffLimits(3,0,0));
    }

    /*
     * 
     * 
     */
    public static int getPossiblePaths(int n, int row, int col) {
	if (row >= n || col >= n) {
	    return 0;
	}
	return 1 + getPossiblePaths(n,row+1,col) + getPossiblePaths(n,row,col+1);
    }

    public static int getPossiblePathsOffLimits(int n, int row, int col) {
	if (row >= n || col >= n) {
	    return 0;
	} else if (offLimitsArr.get(0)[0] == row && offLimitsArr.get(0)[1] == col) {
	    return 0;
	} else {
	    return 1 + getPossiblePathsOffLimits(n,row+1,col) + getPossiblePathsOffLimits(n,row,col+1);
	}
    }

}
