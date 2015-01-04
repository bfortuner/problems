package lists;

import java.util.HashMap;

public class DeleteNode {

    public static void main(String[] args) {
        SinglyLinkedList l1 = new SinglyLinkedList();
        Node head = new Node("A");
        l1.setHead(head);
        Node n1 = new Node("B");
        head.setNext(n1);
        Node n2 = new Node("B");
        n1.setNext(n2);
        Node n3 = new Node("C");
        n2.setNext(n3);
        Node n4 = new Node("C");
        n3.setNext(n4);
        n4.setNext(new Node("B"));
        printLinkedList(l1);
        deleteNode(n2);
        printLinkedList(l1);
    }

    public static void deleteNode(Node node) {
        Node next = node.getNext();
        node.setValue(next.getValue());
        node.setNext(next.getNext());
    }

    public static void printLinkedList(SinglyLinkedList list) {
        Node next = list.getHead();
        while (next != null) {
            System.out.print(next.getValue() + " --> ");
            next = next.getNext();
        }
        System.out.println("");
    }

}
