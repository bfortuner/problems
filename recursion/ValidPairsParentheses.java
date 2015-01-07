package recursion;

public class ValidPairsParentheses {

    public static void main(String[] args) {
	getValidPairs3(3,3,"");
	getValidPairs4(3,3,"");
    }

    public static void getValidPairs3(int left, int right, String cur) {
	if (right == 0) {
	    System.out.println(cur);
	} else if (left == 0) {
	    getValidPairs3(left, right-1, cur+")");	    
	} else if (left == right) { 
	    getValidPairs3(left-1, right, cur+"(");
	} else {
	    getValidPairs3(left-1, right, cur+"(");
	    getValidPairs3(left, right-1, cur+")");
	}
    }


}
