package lists;

public class Node<T> {
	Node next;
    Node prior;
	T value;

    public Node(T value) {
        this.value = value;
    }

    public void setNext(Node next) {
        this.next = next;
    }
	public void setPrior(Node prior) {
		this.prior = prior;
	}
	public void setValue(T value) {
		this.value = value;
	}
	public T getValue() {
		return this.value;
	}
    public Node getNext() {
        return this.next;
    }
    public Node getPrior() {
        return this.prior;
    }
}
