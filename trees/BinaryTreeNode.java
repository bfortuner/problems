package trees;


public class BinaryTreeNode {
    BinaryTreeNode parent;
    BinaryTreeNode leftChild;
    BinaryTreeNode rightChild;
    String key;
    String value;

    public BinaryTreeNode(String key, String value, BinaryTreeNode parent) {
	this.key = key;
	this.value = value;
	this.parent = parent;
    }
    public BinaryTreeNode getParent() {
        return this.parent;
    }
    public void setParent(BinaryTreeNode tree) {
        this.parent = tree;
    }
    public String getKey() {
        return this.key;
    }
    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return this.value;
    }
    public void setValue(String val) {
        this.value = val;
    }
    public void setLeftChild(BinaryTreeNode child) {
	child.setParent(this);
	this.leftChild = child;
    }
    public void setRightChild(BinaryTreeNode child) {
	child.setParent(this);
	this.rightChild = child;
    }
    public BinaryTreeNode getLeftChild() {
	return this.leftChild;
    }
    public BinaryTreeNode getRightChild() {
	return this.rightChild;
    }

}
