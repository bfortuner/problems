package trees;


public class TreeTraversals {


    public static void main(String[] str) {
	BinaryTree tree = new BinaryTree("A");
	BinaryTree t2 = new BinaryTree("B");
	BinaryTree t3 = new BinaryTree("C");
	tree.setLeftChild(t2);
	tree.setRightChild(t3);

	BinaryTree t4 = new BinaryTree("D");
	BinaryTree t5 = new BinaryTree("E");
	t2.setLeftChild(t4);
	t2.setRightChild(t5);

	BinaryTree t6 = new BinaryTree("F");
	BinaryTree t7 = new BinaryTree("G");
	t3.setLeftChild(t6);
	t3.setRightChild(t7);
	System.out.println("preOrder---");
	preOrder(tree);
	System.out.println("inOrder---");
	inOrder(tree);
	System.out.println("postOrder---");
	postOrder(tree);

	/*
	       A
	    B    C
          D  E  F  G
 
	 */

	System.out.println("insertChild---");
	BinaryTree t8 = new BinaryTree("H");
	insertChild(tree, t8);
	System.out.println(tree.getLeftChild().getLeftChild().getLeftChild().getValue());
	preOrder(tree);
	
    }

    public static void preOrder(BinaryTree tree) {
	//A B D E C F G
	if (tree == null) {
	    //skip
	} else {
	    System.out.println(tree.getValue());
	    preOrder(tree.getLeftChild());
	    preOrder(tree.getRightChild());
	}
    }

    public static void inOrder(BinaryTree tree) {
	//D B E A F C G
	if (tree == null) {
	    //skip
	} else {
	    inOrder(tree.getLeftChild());
	    System.out.println(tree.getValue());
	    inOrder(tree.getRightChild());
	}
    }

    public static void postOrder(BinaryTree tree) {
	//D E B F G C A
	if (tree == null) {
	    //skip
	} else {
	    postOrder(tree.getLeftChild());
	    postOrder(tree.getRightChild());
	    System.out.println(tree.getValue());
	}
    }

    public static void insertChild(BinaryTree tree, BinaryTree child) {
	if (tree.getLeftChild() == null) {
	    tree.setLeftChild(child);
	} else if (tree.getRightChild() == null) {
	    tree.setRightChild(child);
	} else {
	    insertChild(tree.getLeftChild(), child);
	    insertChild(tree.getRightChild(), child);
	}
    }

}
