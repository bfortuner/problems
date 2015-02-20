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
	basics.removeLast(n1);
	basics.printLinkedList(n1);
	System.out.println("SIZE = " + basics.getSize(n1));
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


    public void printLinkedList(Node<T> first) {
	while (first != null) {
	    System.out.print(first.value + " --> ");
	    first = first.next;
	}
	System.out.println();
    }

}
