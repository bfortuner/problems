package lists;

import java.util.HashMap;

public class CircularLinkedList {

    public static void main(String[] args) {
        SinglyLinkedList l1 = new SinglyLinkedList();
        Node head = new Node("A");
        l1.setHead(head);
        Node n1 = new Node("B");
        head.setNext(n1);
        Node n2 = new Node("E");
        n1.setNext(n2);
        Node n3 = new Node("C");
        n2.setNext(n3);
        n3.setNext(n1);
        System.out.println(getFirstNode(l1).getValue());
    }

    public static Node getFirstNode(SinglyLinkedList list) {
        HashMap<String,String> map = new HashMap<String,String>();
        Node next = list.getHead();
        while (next != null) {
            if (map.containsKey(next.getValue())) {
                return next;
            } else {
                map.put(next.getValue(),next.getValue());
                next = next.getNext();
            }
        }
        return null;
    }

    public static Node getFirstNodeNoBuffer(SinglyLinkedList list) {
        return null;
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
