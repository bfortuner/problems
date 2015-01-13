package stacks;

public class QueueUsingStacks {

    public static void main(String[] args) {
        QueueUsingStacks queue = new QueueUsingStacks();
        queue.enqueue("hello");
        queue.enqueue("hi");
        System.out.println(queue.dequeue().equals("hello"));
    }
    
    static Stack s1 = new Stack();
    static Stack s2 = new Stack();

    public static void enqueue(String val) {
	String s = s1.pop();
	while (s != null) {
	    s2.push(s);
	    s = s1.pop();
	}
	s1.push(val);
	s = s2.pop();
	while (s != null) {
	    s1.push(s);
	    s = s2.pop();
	}
    }

    public static String dequeue() {
	return s1.pop();
    }

}
