package trees;


import java.util.List;
import java.util.ArrayList;

public class IsSubtree {


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
	BinaryTree t8 = new BinaryTree("H");
	t5.setRightChild(t8);


	BinaryTree t9 = new BinaryTree("O");
	/*
	       A
	    B    C
          D  E  F  G
 
	 */

	int t1height = getHeight(7);
	int t2height = getHeight(0);
	System.out.println(t1height + " " + t2height);
	System.out.println(isSubtree(tree, t4, 0, t1height-t2height) == true);

	t1height = getHeight(7);
	t2height = getHeight(3);
	System.out.println(t1height + " " + t2height);
	System.out.println(isSubtree(tree, t2, 0, t1height-t2height) == true);
	t1height = getHeight(7);
	t2height = getHeight(3);
	System.out.println(isSubtree(tree, t9, 0, t1height-t2height) == false);
    }

    public static boolean isSubtree(BinaryTree t1, BinaryTree t2, int height, int maxHeight) {
	if (t1 == t2) {
	    return true;
	} else if (t1 == null) {
	    return false;
	} else if (height > maxHeight) {
	    return false;
	} else {
	    System.out.println(t1.getValue());
	    boolean left = isSubtree(t1.getLeftChild(), t2, height+1, maxHeight);
	    boolean right = isSubtree(t1.getRightChild(), t2, height+1, maxHeight);
	    if (left || right) {
		return true;
	    } else {
		return false;
	    }
	}
    }

    public static int getHeight(int nodes) {
	int curSum = 0;
	int curHeight = 0;
	while (curSum < nodes) {
	    int add = (int) Math.pow(2,curHeight);
	    curSum = curSum + add;
	    curHeight++;
	}

	return curHeight;
    }




}
