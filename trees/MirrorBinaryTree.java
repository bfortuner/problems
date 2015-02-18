package trees;

public class MirrorBinaryTree {

    public static void main(String[] args) {
	String[] a1 = {"1","2","3","4","5","6","7"};
	BinaryTree t1 = BuildBinarySearchTree.buildBinaryTree(a1);
	BuildBinarySearchTree.printTree(t1);
	System.out.println("============");
	BinaryTree m1 = mirrorTree(t1);
	BuildBinarySearchTree.printTree(m1);
    }


    public static BinaryTree mirrorTree(BinaryTree tree) {
	if (tree == null) {
	    return tree;
	}
	BinaryTree tmp = tree.getLeftChild();
	tree.leftChild = mirrorTree(tree.rightChild);
	tree.rightChild = mirrorTree(tmp);
	return tree;
	
    }


}
