package lists;

public class NodeInteger {
    NodeInteger next;
    NodeInteger prior;
    int value;
    int min;

    public NodeInteger(int value) {
        this.value = value;
    }

    public void setNext(NodeInteger next) {
        this.next = next;
    }
    public void setPrior(NodeInteger prior) {
	this.prior = prior;
    }
    public void setMin(int val) {
	this.min = val;
    }
    public int getMin() {
	return this.min;
    }
    public void setValue(int value) {
	this.value = value;
    }
    public int getValue() {
	return this.value;
    }
    public NodeInteger getNext() {
        return this.next;
    }
    public NodeInteger getPrior() {
        return this.prior;
    }
}
