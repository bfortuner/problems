package queues;

public class Queue {

    public static void main(String[] args) {
        Queue s1 = new Queue();
        s1.enqueue("hello");
        s1.enqueue("hi");
        System.out.println(s1.dequeue().equals("hello"));
    }

    Node first;
    Node last;

    public void enqueue(String val) {
        Node n = new Node(val);
        if (first == null) {
            first = n;
            first.setNext(last);
        } else if (last == null) {
            last = n;
        } else {
            last.setNext(n);
        }
    }

    public String dequeue() {
        if (first == null) {
            return null;
        } else {
            String val = first.getValue();
            first = first.getNext();
            return val;
        }
    }

}
