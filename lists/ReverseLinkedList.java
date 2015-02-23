package lists;

public class ReverseLinkedList<T> {

    public static void main(String[] args) {
	ReverseLinkedList rev = new ReverseLinkedList();
        Node<String> n1 = new Node("A");
        Node<String> n2 = new Node("B");
        Node<String> n3 = new Node("C");
        Node<String> n4 = new Node("D");
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = null;
        rev.printLinkedList(n1);
	Node<String> r1 = rev.reverseIterative(n1);
        rev.printLinkedList(r1);
	Node<String> o1 = rev.reverseRecursive(r1,null);
        rev.printLinkedList(o1);
	Node<String> r2 = rev.reverseRecursive2(o1);
        rev.printLinkedList(r2);
    }

    public Node<T> reverseIterative(Node<T> first) {
	if (first == null) {
	    return null;
	}
	Node<T> last = null;
	Node<T> cur = first;
	while (cur != null) {
	    Node<T> next = cur.next;
	    cur.next = last;
	    last = cur;
	    cur = next;
	}
	return last;
    }

    public Node<T> reverseRecursive(Node<T> cur, Node<T> last) {
	if (cur == null) {
	    return last;
	}
	Node<T> next = cur.next;
	cur.next = last;
	return reverseRecursive(next, cur);
    }

    public Node<T> reverseRecursive2(Node<T> cur) {
	if (cur == null) {
	    return null;
	}
	if (cur.next == null) {
	    return cur;
	}
	Node<T> next = cur.next;
	Node<T> rest = reverseRecursive2(next);
	next.next = cur;
	cur.next = null;
	return rest;
    }

    public void printLinkedList(Node<T> next) {
        while (next != null) {
            System.out.print(next.getValue() + " --> ");
            next = next.getNext();
        }
        System.out.println();
    }

}
