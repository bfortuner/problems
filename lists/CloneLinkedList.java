package lists;

import java.util.*;

public class CloneLinkedList<T> {

    public static void main(String[] args) {
	CloneLinkedList clone = new CloneLinkedList();
	Node<String> n1 = new Node("A");
	Node<String> n2 = new Node("B");
	Node<String> n3 = new Node("C");
	Node<String> n4 = new Node("D");
	n1.next = n2;
	n2.next = n3;
	n3.next = n4;
	n4.next = null;

	n1.random = n3;
	n2.random = n4;
	n3.random = n1;
	n4.random = n2;
	clone.printLinkedList(n1);

	Node<String> copy = clone.getCopyOfList(n1);
	clone.printLinkedList(copy);
    }
    
    public static class Node<T> {
	public T value;
	public Node next;
	public Node random;
	public Node(T val) {
	    this.value = val;
	}
    }

    public Node<T> getCopyOfList(Node<T> firstOrg) {
	List<Node<T>> orgs = new ArrayList();
	List<Node<T>> copies = new ArrayList();
	Node<T> firstCopy = new Node(firstOrg.value);
	Node<T> org = firstOrg;
	Node<T> copy = firstCopy;
	while (org.next != null) {	    
	    Node<T> newCopy = new Node(org.next.value);
	    copy.next = newCopy;
	    copies.add(copy);
	    orgs.add(org);
	    copy = copy.next;
	    org = org.next;
	}
	copies.add(copy);
	orgs.add(org);

	copy = firstCopy;
	org = firstOrg;
	while (org != null) {
	    int randIndex = orgs.indexOf(org.random);
	    copy.random = orgs.get(randIndex);
	    org = org.next;
	    copy = copy.next;
	}
	return firstCopy;
    }

    public void printLinkedList(Node<T> first) {
	while (first != null) {
	    System.out.print(first.value + "(" + first.random.value + ")" + " --> ");
	    first = first.next;
	}
	System.out.println();
    }

}
