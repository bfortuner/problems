package stacks;

public class TowersOfHanoi {

    static Stack s1 = new Stack();
    static Stack s2 = new Stack();
    static Stack s3 = new Stack();

    public static void main(String[] args) {
	s1.push("c");
	s1.push("b");
	s1.push("a");
	hanoi(3, 1, "right");
	System.out.println("first ---- ");
	while (!s1.isEmpty()) {
	    System.out.println(s1.pop());
	}
	System.out.println("second ---- ");
	while (!s2.isEmpty()) {
	    System.out.println(s2.pop());
	}
	System.out.println("third ---- ");
	while (!s3.isEmpty()) {
	    System.out.println(s3.pop());
	}
    }

    public static void hanoi(int n, int pos, String direction) {
	if (s1.isEmpty() && s2.isEmpty()) {
	    //do nothing
	} else {
	    if ( direction.equals("right") ) {
		if (pos == 3) {
		    hanoi(n,1,"right");
		} else if (pos == 2 && !s2.isEmpty() ) {
		    if ( s3.isEmpty() ) {
			System.out.println("2 --> 3");
			s3.push(s2.pop());
			hanoi(n,1,"right");
		    } else if ( lessThan(s2.peek(), s3.peek()) ) {
			System.out.println("2 --> 3");
			s3.push(s2.pop());
			hanoi(n,1,"right");
		    } else {
			hanoi(n,3,"left");
			System.out.println("2 --> 3");
			s3.push(s2.pop());
			hanoi(n,3,"right");
		    }
		} else if ( pos == 1 && !s1.isEmpty() ) {
		    System.out.println("1 --> 2");
		    s2.push(s1.pop());
		    hanoi(n,2,"right");
		} else {
		    //hanoi(n,1,"right");
		}
	    } else {
		if (pos == 1) {
		    hanoi(n,3,"left");
		} else if (pos == 2) {
		    if ( s1.isEmpty() || lessThan(s2.peek(), s1.peek()) ) {
			System.out.println("2 --> 1");
			s1.push(s2.pop());
			hanoi(n,3,"left");
		    } else {
			hanoi(n,1,"right");
		    }
		} else if ( pos == 3 && !s3.isEmpty() ) {
		    System.out.println("3 --> 2");
		    s2.push(s3.pop());
		    hanoi(n,2,"left");
		} else {
		    //do nothing
		}
	    }

	}
    }

    private static boolean lessThan(String a, String b) {
	return a.compareTo(b) < 0;
    }



}
