package lists;

import java.util.HashMap;

public class RemoveDuplicates {

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
        removeDuplicatesLoops(l1);
        printLinkedList(l1);
    }

    public static void removeDuplicates(SinglyLinkedList list) {
        HashMap<String,String> map = new HashMap<String,String>();
        Node prior = list.getHead();
        Node next = list.getHead();
        while (next != null) {

            if (!map.containsKey(next.getValue())) {
                map.put(next.getValue(), "Exists");
                prior = next;
                next = next.getNext();
            } else {
                next = next.getNext();
                prior.setNext(next);
            }
        }

    }


    public static void removeDuplicatesLoops(SinglyLinkedList list) {
        Node cur = list.getHead();
        while (cur != null) {
            String val = cur.getValue();
            Node prior = cur;
            Node next = cur.getNext();
            while (next != null) {
                if (next.getValue().equals(val)) {
                    next = next.getNext();
                    prior.setNext(next);
                } else {
                    prior = next;
                    next = next.getNext();
                }
            }
            cur = cur.getNext();
        }
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
