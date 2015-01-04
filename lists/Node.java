package lists;

public class Node {
	Node next;
    Node prior;
	String value;

    public Node(String value) {
        this.value = value;
    }

    public void setNext(Node next) {
        this.next = next;
    }
	public void setPrior(Node prior) {
		this.prior = prior;
	}
	public void setValue(String value) {
		this.value = value;
	}
	public String getValue() {
		return this.value;
	}
    public Node getNext() {
        return this.next;
    }
    public Node getPrior() {
        return this.prior;
    }
}
