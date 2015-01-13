package stacks;

public class SetOfStacks {

    public static void main(String[] args) {
        SetOfStacks s1 = new SetOfStacks();
	s1.push("hello");
	s1.push("hello1");
	s1.push("hello2");
	s1.push("hello3");
	s1.push("hello4");
	s1.push("hello5");
	System.out.println(plates);
	System.out.println(curStack);

	System.out.println(s1.pop());
	System.out.println(plates);
	System.out.println(curStack);
    }

    static Stack[] set = new Stack[8];
    static int THRESHOLD = 5;
    static int curStack = 0;
    static int plates = 0;

    public static void push(String val) {
	if (set[curStack] == null) {
	    set[curStack] = new Stack();
	    set[curStack].push(val);
	    plates++;
	} else if (plates == THRESHOLD) {
	    curStack++;
	    plates = 0;
	    push(val);
	} else {
	    set[curStack].push(val);
	    plates++;
	}
    }

    public static String pop() {
	if (plates == 0) {
	    curStack--;
	    plates = 5;
	    return pop();
	} else {
	    plates--;
	    return set[curStack].pop();
	}
    }

}
