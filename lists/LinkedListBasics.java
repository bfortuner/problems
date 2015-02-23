package lists;

import java.util.*;

public class LinkedListBasics<T> {

    public static void main(String[] args) {
	LinkedListBasics basics = new LinkedListBasics();
	Node<String> n1 = new Node("A");
	Node<String> n2 = new Node("B");
	Node<String> n3 = new Node("C");
	Node<String> n4 = new Node("D");
	n1.next = n2;
	n2.next = n3;
	n3.next = n4;
	n4.next = null;
	basics.printLinkedList(n1);
	System.out.println("SIZE = " + basics.getSize(n1));

	//Test Remove Last
	//basics.removeLast(n1);
	//basics.printLinkedList(n1);
	//System.out.println("SIZE = " + basics.getSize(n1));

	//Test Remove Kth Element
	//basics.deleteKthNode(n1,2);
	//basics.printLinkedList(n1);
	//System.out.println("SIZE = " + basics.getSize(n1));

	//Test Contains Element
	//System.out.println(basics.containsElement(n1,"C") == true);
	//System.out.println(basics.containsElement(n1,"J") == false);

	//Test Remove After
	//basics.removeAfter(n2);
	//basics.printLinkedList(n1);
	//System.out.println("SIZE = " + basics.getSize(n1));

	//Test Insert After
	//Node<String> n5 = new Node("NEWGUY");
	//basics.insertAfter(n2,n5);
	//basics.printLinkedList(n1);
	//System.out.println("SIZE = " + basics.getSize(n1));

	//Test Remove by Key
	//Node<String> n6 = new Node("B");
	//basics.insertAfter(n3,n6);
	//basics.printLinkedList(n1);
	//basics.removeByKey(n1,"B");
	//basics.printLinkedList(n1);

	//Test Get Max
	//Node<String> n7 = new Node("Z");
	//basics.insertAfter(n3,n7);
	//System.out.println(basics.getMax(n1).equals("Z"));

	//Test Get Max Recursive
	Node<String> n8 = new Node("Z");
	basics.insertAfter(n3,n8);
	System.out.println(basics.getMaxRecursive(n1).equals("Z"));

    }
    
    public static class Node<T> {
	public T value;
	public Node next;
	public Node(T val) {
	    this.value = val;
	}
    }
    
    public void removeLast(Node<T> first) {
	Node last = first;
	Node cur = first;
	while (cur.next != null) {
	    last = cur;
	    cur = cur.next;
	}
	last.next = null;
    }

    public int getSize(Node<T> first) {
	int size = 0;
	while (first != null) {
	    size++;
	    first = first.next;
	}
	return size;
    }

    public void deleteKthNode(Node<T> first, int k) {
	Node<T> last = null;
	Node<T> cur = first;
	int i = 1;
	while (i < k) {
	    last = cur;
	    cur = cur.next;
	    i++;		
	}
	if (cur != null) {
	    last.next = cur.next;
	} else {
	    last.next = null;
	}
    }

    public boolean containsElement(Node<T> first, T key) {
	while (first != null) {
	    if (first.value.equals(key)) {
		return true;
	    }
	    first = first.next;
	}
	return false;
    }

    public void removeAfter(Node<T> first) {
	if (first != null && first.next != null) {
	    first.next = first.next.next;
	}
    }

    public void insertAfter(Node<T> first, Node<T> newNode) {
	if (first != null && newNode != null) {
	    newNode.next = first.next;
	    first.next = newNode;
	}
    }

    public void removeByKey(Node<T> first, T key) {
	Node<T> last = first;
	Node<T> cur = first;
	while (cur != null) {
	    if (cur.value.equals(key)) {
		last.next = cur.next;
		cur = cur.next;
	    } else {
		last = cur;
		cur = cur.next;
	    }
	}
    }

    public T getMax(Node<T> first) {
	if (first == null) {
	    return null;
	}
	T max = first.value;
	while (first != null) {
	    if (compareGenericVals(first.value,max) > 0) {
		max = first.value;
	    }
	    first = first.next;
	}
	return max;
    }

    public T getMaxRecursive(Node<T> first) {
	if (first == null) {
	    return null;
	}
	T max = getMaxRecursive(first.next);
	if (max != null) {
	    if (compareGenericVals(first.value,max) > 0) {
		return first.value;
	    }
	    return max;
	}
	return first.value;
    }

    //Returns -1, 0, or 1 (less, equal, greater)
    //Helper Function To Compare Generics
    private int compareGenericVals(T val1, T val2) {
	try {
	    String s1 = (String) val1;
	    String s2 = (String) val2;
	    return s1.compareTo(s2);
	} catch (ClassCastException e) {
	    Integer i1 = (Integer) val1;
	    Integer i2 = (Integer) val2;
	    if (i1 > i2) {
		return 1;
	    } else if (i1 == i2) {
		return 0;
	    } else {
		return -1;
	    }
	}
    }

    public void printLinkedList(Node<T> first) {
	while (first != null) {
	    System.out.print(first.value + " --> ");
	    first = first.next;
	}
	System.out.println();
    }

}
