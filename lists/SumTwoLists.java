package lists;

import java.util.HashMap;

public class SumTwoLists {

    public static void main(String[] args) {
        SinglyLinkedListInteger l1 = new SinglyLinkedListInteger();
        NodeInteger head = new NodeInteger(4);
        l1.setHead(head);
        NodeInteger n1 = new NodeInteger(8);
        head.setNext(n1);
        NodeInteger n2 = new NodeInteger(5);
        n1.setNext(n2);
        NodeInteger n3 = new NodeInteger(6);
        n2.setNext(n3);
        printLinkedList(l1);

        SinglyLinkedListInteger l2 = new SinglyLinkedListInteger();
        NodeInteger head2 = new NodeInteger(0);
        l2.setHead(head2);
        NodeInteger n4 = new NodeInteger(1);
        head2.setNext(n4);
        NodeInteger n5 = new NodeInteger(1);
        n4.setNext(n5);
        NodeInteger n6 = new NodeInteger(5);
        n5.setNext(n6);
        printLinkedList(l2);

        SinglyLinkedListInteger l3 = sumLists(l1, l2);
        printLinkedList(l3);
    }

    public static SinglyLinkedListInteger sumLists(SinglyLinkedListInteger a, SinglyLinkedListInteger b) {
        SinglyLinkedListInteger newList = new SinglyLinkedListInteger();
        int sum = 0;
        int carry = 0;
        NodeInteger nodeA = a.getHead();
        NodeInteger nodeB = b.getHead();
        NodeInteger newNode = new NodeInteger(carry);
        newList.setHead(newNode);
        while (nodeA != null && nodeB != null) {
            sum = nodeA.getValue() + nodeB.getValue();
            carry = sum / 10;
            newNode.setValue(newNode.getValue() + (sum % 10) );
            newNode.setNext(new NodeInteger(carry));
            newNode = newNode.getNext();
            nodeA = nodeA.getNext();
            nodeB = nodeB.getNext();
        }
        return newList;
    }

    public static void printLinkedList(SinglyLinkedListInteger list) {
        NodeInteger next = list.getHead();
        while (next != null) {
            System.out.print(next.getValue() + " --> ");
            next = next.getNext();
        }
        System.out.println("");
    }

}
