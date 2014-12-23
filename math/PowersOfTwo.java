public class PowersOfTwo {

    public static void main(String[] args) {
    	int in = 3;
    	int out = 256;
    	System.out.println(getPowerOfTwo(in) == out);
    }

    /* 
     * Compute 2^2^n in linear time
     */
    public static int getPowerOfTwo(int n) {
    	if (n == 0) {
    		return 2;
    	} else {
    		return getPowerOfTwo(n-1) * getPowerOfTwo(n-1);
    	}
    }

}
