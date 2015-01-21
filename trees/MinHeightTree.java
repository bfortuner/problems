package trees;

import java.lang.Math;

public class MinHeightTree {


    public static void main(String[] str) {
	BinaryTree tree = new BinaryTree("");
	String[] arr = {"A","B","C","D","E"};
	BinaryTree newTree = buildTree(tree,arr,0,arr.length);
	printTree(newTree);
	
    }

    public static BinaryTree buildTree(BinaryTree tree, String[] arr, int start, int end) {
	if (end-start == 0) {
	    return tree;
	} else if (end-start == 1) {
	    tree.setValue(arr[0]);
	    return tree;
	} else if (end-start == 2) {
	    tree.setValue(arr[0]);
	    tree.setLeftChild(new BinaryTree(arr[1]));
	    return tree;
	} else {
	    int mid = start + (end-start)/2;
	    tree.setValue(arr[mid]);
	    BinaryTree left = buildTree(new BinaryTree(""), arr, start, mid);
	    BinaryTree right = buildTree(new BinaryTree(""), arr, mid+1, end);
	    tree.setLeftChild(left);
	    tree.setRightChild(right);
	    return tree;
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
