package trees;


public class BinaryTree<T> {
    BinaryTree parent;
    BinaryTree leftChild;
    BinaryTree rightChild;
    T value;
    int subtreeWeight;

    public BinaryTree(T value) {
	this.value = value;
    }
    public BinaryTree getParent() {
        return this.parent;
    }
    public void setParent(BinaryTree tree) {
        this.parent = tree;
    }
    public T getValue() {
        return this.value;
    }
    public void setValue(T val) {
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

    public int getSubtreeWeight() {
	return this.subtreeWeight;
    }

    public void setSubtreeWeight(int weight) {
	this.subtreeWeight = weight;
    }

}
