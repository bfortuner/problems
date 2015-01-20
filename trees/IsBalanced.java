package trees;

import java.lang.Math;

public class IsBalanced {


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

	/*
	       A
	    B    C
          D  E  F  G

	 */
	BinaryTree t8 = new BinaryTree("K");
	t4.setRightChild(new BinaryTree("J"));
	t6.setRightChild(t8);
	t8.setRightChild(new BinaryTree("I"));
	System.out.println(getHeight(tree) == 5);
	System.out.println(isBalanced(tree) == true);
    }

    public static boolean isBalanced(BinaryTree tree) {
	if (tree == null) {
	    return true;
	} else {
	    int left = getHeight(tree.getLeftChild());
	    int right = getHeight(tree.getRightChild());
	    if (Math.abs(left - right) > 1) {
		return false;
	    } else {
		return true;
	    }
	}
    }

    public static int getHeight(BinaryTree tree) {
	if (tree == null) {
	    return 0;
	} else {
	    int left = getHeight(tree.getLeftChild());
	    int right = getHeight(tree.getRightChild());
	    if (left > right) {
		return left + 1;
	    } else {
		return right + 1;
	    }
	}
    }


}
