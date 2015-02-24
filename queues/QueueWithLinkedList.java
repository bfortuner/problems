package queues;

import lists.Node;

public class QueueWithLinkedList<T> {

    public static void main(String[] args) {
        QueueWithLinkedList<String> queue = new QueueWithLinkedList();
        queue.enqueue("A");
        queue.enqueue("B");
        queue.enqueue("C");
        //System.out.println(queue.dequeue());
        //System.out.println(queue.dequeue());
        //System.out.println(queue.dequeue());

	Node<String> t1 = new Node("A");
	Node<String> t2 = new Node("B");
	Node<String> t3 = new Node("C");
	queue.testAssignment(t1,t2);
	System.out.println((t1.value == t2.value) == true);

	t1.next = t2;
	t2.next = t3;
	t2 = t3;
	System.out.println(t1.next.value);

	/*
	Node<String> new1 = queue.testObjectAssignment(t1,t2);
	System.out.println(new1.value);
	System.out.println(new1.next.value);
	*/

    }

    Node<T> last;

    public void enqueue(T val) {
        Node<T> n = new Node(val);
        if (last == null) {
	    last = n;
        } else if (last.next == null) {
	    n.next = last;
	    last.next = n;
	    last = n;
	} else {
	    n.next = last.next;
	    last.next = n;
	    last = n;
	}
    }

    public T dequeue() {
        if (last == null) {
            return null;
        }
	if (last.next == null) {
	    Node<T> first = last;
	    last = null;
	    return first.value;
	}
	Node<T> first = last.next;
	last.next = first.next;
	return first.value;
    }

    public void testAssignment(Node<T> t1, Node<T> t2) {
	t1.value = t2.value;
    }

    public Node<String> testObjectAssignment(Node<String> t1, Node<String> t2) {
	Node<String> t3 = new Node("C");
	t1.next = t2;
	t2.next = t3;
	t2 = t3;
	return t1;
    }

}

