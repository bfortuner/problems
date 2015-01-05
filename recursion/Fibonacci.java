package recursion;


public class Fibonacci {

    public static void main(String[] args) {
	int fib = fibonacci(10);
	System.out.println(fib == 55);
    }

    /*
     * Fn = F(n-1) + F(n-2)
     * F(1) == 1, F(0) == 0 
     */
    public static int fibonacci(int n) {
	if (n == 0) {
	    return 0;
	} else if (n == 1) {
	    return 1;
	} else {
	    return fibonacci(n-1) + fibonacci(n-2);
	}
    }

}
