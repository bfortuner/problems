package trees;


import java.util.List;
import java.util.ArrayList;

public class FirstAncestor {


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

	/*
	       A
	    B    C
          D  E  F  G
 
	 */
	System.out.println(getFirstAncestorArray(t6, t7) == t3);
	System.out.println(getFirstAncestorArray(t8, t4) == t2);
	System.out.println(getFirstAncestorArray(t8, t7) == tree);	

	System.out.println(getFirstAncestor(t6, t7) == t3);
	System.out.println(getFirstAncestor(t8, t4) == t2);
	System.out.println(getFirstAncestor(t8, t7) == tree);	
    }

    /*
     * Find first common parent of 2 nodes in Tree
     * Technique - No additional data structure
     */
    public static BinaryTree getFirstAncestor(BinaryTree t1, BinaryTree t2) {
	BinaryTree p1 = t1.getParent();
	while (p1 != null) {
	    boolean inChain = checkInParentChain(p1, t2);
	    if (inChain) {
		return p1;
	    } else {
		p1 = p1.getParent();
	    }
	}

	BinaryTree p2 = t2.getParent();
	while (p2 != null) {
	    boolean inChain = checkInParentChain(p2, t1);
	    if (inChain) {
		return p2;
	    } else {
		p2 = p2.getParent();
	    }
	}
	return null;
    }

    /*
     * Is t1 in parent chain of t2?
     */
    public static boolean checkInParentChain(BinaryTree t1, BinaryTree t2) {
	while (t2 != null) {
	    if (t2 == t1) {
		return true;
	    }
	    t2 = t2.getParent();
	}
	return false;
    }

    /*
     * Find first common parent of 2 nodes in Tree
     * Technique - Store all parents of node 2 in array
     * Move up parent chain of node1 and check for first parent in node 2 array
     */
    public static BinaryTree getFirstAncestorArray(BinaryTree t1, BinaryTree t2) {
	List<BinaryTree> l1 = new ArrayList();
	while (t2.getParent() != null) {
	    l1.add(t2.getParent());
	    t2 = t2.getParent();
	}
	BinaryTree firstParent = null;
	BinaryTree parent = t1.getParent();
	while (firstParent == null && parent != null) {
	    for (BinaryTree tree : l1) {
		if (parent == tree) {
		    firstParent = parent;
		}
	    }
	    parent = parent.getParent();
	}
	return firstParent;
    }



}
