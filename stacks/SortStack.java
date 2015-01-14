package stacks;

public class SortStack {

    public static void main(String[] args) {
	Stack s1 = new Stack();
        System.out.println(s1.isEmpty() == true);
	s1.push("b");
	s1.push("c");
	s1.push("d");
	s1.push("a");
	s1.push("a");
	s1.push("e");
	s1 = sortStack(s1);
	while (!s1.isEmpty()) {
	    System.out.println(s1.pop());
	}
    }
    
    public static Stack sortStack(Stack stack) {
	Stack tmp = new Stack();
	Stack sorted = new Stack();
	while (!stack.isEmpty()) {
	    while ( !sorted.isEmpty() && greaterThan(stack.peek(), sorted.peek()) ) {
		tmp.push(sorted.pop());
	    }
	    sorted.push(stack.pop());
	    while ( !tmp.isEmpty() ) {
		sorted.push(tmp.pop());
	    }
	}

	return sorted;
    }

    private static boolean greaterThan(String a, String b) {
	return a.compareTo(b) > 0;
    }

}
