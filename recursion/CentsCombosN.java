package recursion;

public class CentsCombosN {

    public static void main(String[] args) {
	int[] cents = {25,10,5,1};
	int n = 25;
	int res = getPossibleNCombos(0, cents, 0, n);
	System.out.println(res);
   }

    public static int getPossibleNCombos(int sum, int[] cents, int index, int n) {
	if (sum == n) {
	    return 1;
	} else if (index > cents.length-1) {
	    return 0;
	} else if (sum + cents[index] > n) {
	    return getPossibleNCombos(sum, cents, index+1, n); 
	} else {
	    return getPossibleNCombos(sum+cents[index], cents, index, n) +
		getPossibleNCombos(sum, cents, index+1, n); 
	}
    }

}
