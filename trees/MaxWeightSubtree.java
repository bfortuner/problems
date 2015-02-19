package trees;

public class MaxWeightSubtree {

    public static void main(String[] args) {
	int[] a1 = {1,2,-1,-1,5,0};
	BinaryTree<Integer> t1 = new BinaryTree(1);
	BinaryTree<Integer> t2 = new BinaryTree(2);
	BinaryTree<Integer> t3 = new BinaryTree(-1);
	BinaryTree<Integer> t4 = new BinaryTree(-2);
	BinaryTree<Integer> t5 = new BinaryTree(5);
	BinaryTree<Integer> t6 = new BinaryTree(0);
	t1.setLeftChild(t2);
	t1.setRightChild(t3);
	t2.setLeftChild(t4);
	t3.setLeftChild(t5);
	t3.setRightChild(t6);

	System.out.println("============");
	BinaryTree<Integer> m1 = getMaxWeightSubtree(t1);
	System.out.println(m1.getSubtreeWeight() == 5);
	System.out.println("============");
    }

    public static BinaryTree<Integer> getMaxWeightSubtree(BinaryTree<Integer> tree) {
	//updates tree so each node keeps track of the weight of its subtree
	int weight = calculateWeights(tree);
	return maxWeightSubtree(tree);
    }

    public static BinaryTree<Integer> maxWeightSubtree(BinaryTree<Integer> tree) {
	if (tree == null) {
	    BinaryTree<Integer> newTree = new BinaryTree<Integer>(0);
	    newTree.setSubtreeWeight(Integer.MIN_VALUE);
	    return newTree;
	}
	BinaryTree<Integer> left = maxWeightSubtree(tree.getLeftChild());
	BinaryTree<Integer> right = maxWeightSubtree(tree.getRightChild());
	if (left.subtreeWeight > right.subtreeWeight && left.subtreeWeight > tree.subtreeWeight) {
	    return left;
	} else if (right.subtreeWeight > left.subtreeWeight && right.subtreeWeight > tree.subtreeWeight) {
	    return right;
	} else {
	    return tree;
	}
    }

    /*
     * Visit all nodes in tree and add tree.weight
     * attribute which keeps track of the weight of
     * all the nodes in that subtree
     */
    public static int calculateWeights(BinaryTree<Integer> tree) {
	if (tree == null) {
	    return 0;
	}
	int leftWeight = calculateWeights(tree.getLeftChild());
	int rightWeight = calculateWeights(tree.getRightChild());
	tree.setSubtreeWeight(tree.value + leftWeight + rightWeight);
	return tree.getSubtreeWeight();
    }


}
