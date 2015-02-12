package trees;

public class BuildBinarySearchTree {

    public static void main(String[] args) {
	String[] a1 = {"A","C","D","F","S"};
	BinaryTree t1 = buildBinaryTree(a1);
	printTree(t1);
	System.out.println("===========");
	String[] a2 = {"C","E","D","A","B"};
	BinaryTree t2 = buildBinaryTree(a2);
	printTree(t2);
    }


    //Create binary search tree from array of Strings
    //[3,6,2,5,7]
    public static BinaryTree buildBinaryTree(String[] arr) {
	BinaryTree tree = new BinaryTree(null);
	for (int i=0; i<arr.length; i++) {
	    put(tree, arr[i]);
	}
	return tree;
    }

    public static void put(BinaryTree tree, String val) {
	BinaryTree cur = tree;
	if (cur.getValue() == null) {
	    cur.setValue(val);
	} else {
	    boolean found = false;
	    BinaryTree child = new BinaryTree(val);
	    while (!found) {
		if (val.compareTo(cur.getValue()) <= 0) {
		    if (cur.getLeftChild() == null) {
			cur.setLeftChild(child);
			found = true;
		    } else {
			cur = cur.getLeftChild();
		    }
		} else {
		    if (cur.getRightChild() == null) {
			cur.setRightChild(child);
			found = true;
		    } else {
			cur = cur.getRightChild();
		    }
		}
	    }
	}
    }

    public static void printTree(BinaryTree tree) {
	if (tree == null) {
	    //do nothing
	} else {
	    System.out.println(tree.getValue());
	    printTree(tree.getLeftChild());
	    printTree(tree.getRightChild());
	}
    }

}
