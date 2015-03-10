package stacks;

public class StackWithMax<T extends Comparable<T>> {

    public static void main(String[] args) {
        StackWithMax<Integer> stack = new StackWithMax<Integer>();
	stack.push(1);
	stack.push(0);
	stack.push(2);
	stack.push(4);
	stack.push(1);
	System.out.println(stack.peek());
	System.out.println(stack.getMax());
	stack.printStack(stack.maxHead);

	System.out.println(stack.pop() == 1);
	System.out.println(stack.getMax() == 4);
	System.out.println(stack.pop() == 4);
	System.out.println(stack.getMax() == 2);
	stack.printStack(stack.maxHead);
    }

    Node<T> stackHead;
    Node<T> maxHead;
    
    public static class Node<T> {
	public Node<T> next;
	public T val;
	public Node(T value) {
	    this.val = value;
	}
    }
    
    public void push(T val) {
	Node<T> newNode = new Node(val);
	newNode.next = stackHead;
	stackHead = newNode;
	addMax(val);
    }

    private void addMax(T val) {
	Node<T> newMax = new Node(val);
	if (maxHead == null) {
	    maxHead = newMax;
	} else if (val.compareTo(maxHead.val) > 0) {
	    newMax.next = maxHead;
	    maxHead = newMax;
	} else {
	    Node<T> last = maxHead;
	    Node<T> cur = maxHead.next;
	    while (cur != null && val.compareTo(cur.val) < 0) {
		last = cur;
		cur = cur.next;
	    }
	    newMax.next = cur;
	    last.next = newMax;
	}
    }

    public T pop() {
	if (stackHead == null) {
	    return null;
	}
	T val = stackHead.val;
	stackHead = stackHead.next;
	removeMax(val);
	return val;
    }

    private void removeMax(T val) {
	if (maxHead.val == val) {
	    maxHead = maxHead.next;
	} else {
	    Node<T> last = maxHead;
	    Node<T> cur = maxHead.next;
	    while (cur.val != val) {
		last = cur;
		cur = cur.next;
	    }
	    last.next = cur.next;
	}
    }

    public T peek() {
	if (stackHead == null) {
	    return null;
	} else {
	    return stackHead.val;
	}
    }

    public T getMax() {
	if (stackHead == null) {
	    return null;
	} else {
	    return maxHead.val;
	}
    }

    public void printStack(Node<T> node) {
	System.out.println();
	while (node != null) {
	    System.out.print(node.val + " --> ");
	    node = node.next;
	}
	System.out.println();
    }

}
