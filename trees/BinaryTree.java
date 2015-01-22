package trees;


public class BinaryTree {
    BinaryTree parent;
    BinaryTree leftChild;
    BinaryTree rightChild;
    String value;

    public BinaryTree(String value) {
	this.value = value;
    }
    public BinaryTree getParent() {
        return this.parent;
    }
    public void setParent(BinaryTree tree) {
        this.parent = tree;
    }
    public String getValue() {
        return this.value;
    }
    public void setValue(String val) {
        this.value = val;
    }
    public void setLeftChild(BinaryTree child) {
	child.setParent(this);
	this.leftChild = child;
    }
    public void setRightChild(BinaryTree child) {
	child.setParent(this);
	this.rightChild = child;
    }
    public BinaryTree getLeftChild() {
	return this.leftChild;
    }
    public BinaryTree getRightChild() {
	return this.rightChild;
    }

}
