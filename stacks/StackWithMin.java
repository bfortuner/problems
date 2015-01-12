package stacks;

import lists.NodeInteger;

public class StackWithMin {

    public static void main(String[] args) {
        StackWithMin s1 = new StackWithMin();
        s1.push(3);
        s1.push(6);
        System.out.println(s1.getMin() == 3);
        System.out.println(s1.pop() == 6);
        System.out.println(s1.getMin() == 3);
        System.out.println(s1.pop() == 3);
        System.out.println(s1.pop() == -1);
    }

    private NodeInteger top;

    public void push(int val) {
        NodeInteger n = new NodeInteger(val);
        if (top == null) {
	    n.setMin(val);
        } else if (val < top.getMin()) {
	    n.setMin(val);
        } else {
	    n.setMin(top.getMin());
        }
	n.setNext(top);
	top = n;
    }

    public int pop() {
        if (top == null) {
            return -1;
        } else {
            int val = top.getValue();
            top = top.getNext();
            return val;
        }
    }

    public int getMin() {
        if (top == null) {
            return -1;
        } else {
            return top.getMin();
        }
    }

}
