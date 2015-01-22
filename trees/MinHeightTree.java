package trees;

import java.lang.Math;
import java.util.List;
import java.util.ArrayList;

public class MinHeightTree {


    public static void main(String[] str) {
	BinaryTree tree = new BinaryTree("");
	List<String> list = new ArrayList();
	String[] arr = {"A","B","C","D","E"};
	for (String s : arr) {
	    list.add(s);
	}
	BinaryTree newTree = buildTree(tree,list);
	printTree(newTree);
	
    }

    public static BinaryTree buildTree(BinaryTree tree, List<String> list) {
	if (list.size() == 0) {
	    return null;
	} else if (list.size() == 1) {
	    return new BinaryTree(list.get(0));
	} else {
	    int mid = list.size() / 2;
	    BinaryTree newTree = new BinaryTree(list.get(mid));
	    newTree.setLeftChild(buildTree(newTree, list.subList(0,mid)));
	    if (mid+1 < list.size()) {
		newTree.setRightChild(buildTree(newTree, list.subList(mid+1,list.size())));
	    }
	    return newTree;
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
