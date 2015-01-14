package stacks;

public class Stack {

    public static void main(String[] args) {
        Stack s1 = new Stack();
        s1.push("hello");
        s1.push("hi");
        System.out.println(s1.isEmpty() == false);
        System.out.println(s1.peek().equals("hi"));
        System.out.println(s1.pop().equals("hi"));
        System.out.println(s1.pop().equals("hello"));
        System.out.println(s1.isEmpty() == true);
    }

    Node top;

    public void push(String val) {
        Node n = new Node(val);
        if (top == null) {
            top = n;
        } else {
            n.setNext(top);
            top = n;
        }
    }

    public String pop() {
        if (top == null) {
            return null;
        } else {
            String val = top.getValue();
            top = top.getNext();
            return val;
        }
    }

    public String peek() {
        if (top == null) {
            return null;
        } else {
            return top.getValue();
        }
    }

    public boolean isEmpty() {
	return top == null;
    }

}
