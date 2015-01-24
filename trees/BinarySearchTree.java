package trees;


public class BinarySearchTree {
    BinaryTreeNode root;
    int size;

    public static void main(String[] args) {
	BinarySearchTree t1 = new BinarySearchTree();
	t1.put("B","BB");
	t1.put("A","AA");
	t1.put("C","CC");
	t1.put("E","EE");
	t1.put("D","DD");

	t1.printTree(t1.getRoot());

	System.out.println(t1.get("E").equals("EE"));
	System.out.println(t1.get("A").equals("AA"));
	System.out.println(t1.get("B").equals("BB"));
    }

    public BinarySearchTree() {
	this.size = 0;
    }

    public BinaryTreeNode getRoot() {
	return this.root;
    }

    public void put(String key, String value) {
	if (this.root == null) {
	    this.root = new BinaryTreeNode(key, value, null);
	} else {
	    _put(key, value, this.root);
	}
    } 

    public void _put(String key, String value, BinaryTreeNode parent) {
	if (key.compareTo(parent.getKey()) < 0) {
	    if (parent.getLeftChild() == null) {
		parent.setLeftChild(new BinaryTreeNode(key, value, parent));
		this.size++;
	    } else {
		_put(key, value, parent.getLeftChild());
	    }

	} else {
	    if (parent.getRightChild() == null) {
		parent.setRightChild(new BinaryTreeNode(key, value, parent));
		this.size++;
	    } else {
		_put(key, value, parent.getRightChild());
	    }
	}
    }

    public String get(String key) {
	if (this.root == null) {
	    return null;
	} else {
	    return _get(key, this.root).getValue();
	}
    }

    public BinaryTreeNode _get(String key, BinaryTreeNode parent) {
	if (parent.getKey() == key) {
	    return parent;
	} else if (key.compareTo(parent.getKey()) < 0) {
	    return _get(key, parent.getLeftChild());
	} else {
	    return _get(key, parent.getRightChild());
	}
    }

    public void delete(String key) {
	
	BinaryTreeNode node = _get(key, this.root);
	BinaryTreeNode parent = node.getParent();
	if (node == parent.getLeftChild()) {
	    if (node.getLeftChild() == null && node.getRightChild() == null) {
		parent.setLeftChild(null);
	    } else if (node.getLeftNode() == null) {
		parent.setLeftChild(node.getRightChild());
	    } else if (node.getRightNode() == null) {
		parent.setLeftChild(node.getLeftChild());
	    } else {
		parent.setLeftChild(node.getLeftChild());
		node.getLeftChild().setRightChild(node.getRightChild());
	    }
	} else {

	}
    }

    public void printTree(BinaryTreeNode tree) {
        if (tree == null) {
            //do nothing
        } else {
            System.out.println(tree.getKey());
            printTree(tree.getLeftChild());
            printTree(tree.getRightChild());
        }
    }


}
