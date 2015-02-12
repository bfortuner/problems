package trees;

public class PrintPathToKey {

    public static void main(String[] args) {
	String[] a1 = {"D","A","B","F","S","C","E"};
	BinaryTree t1 = BuildBinarySearchTree.buildBinaryTree(a1);
	System.out.println(getPathArray(t1,"A").equals("1"));
	System.out.println(getPathArray(t1,"C").equals("100"));
	System.out.println(getPathArray(t1,"E").equals("01"));
	System.out.println(getPathArray(t1,"K").equals("-1"));
    }


    public static String getPathArray(BinaryTree tree, String key) {
	String path = "";
	BinaryTree curNode = tree;
	while(curNode != null) {
	    if (curNode.getValue().equals(key)) {
		return path;
	    } else if ( key.compareTo(curNode.getValue()) <= 0 ) {
		path = path + "1";
		curNode = curNode.getLeftChild();
	    } else {
		path = path + "0";
		curNode = curNode.getRightChild();
	    }
	}
	return "-1";

    }

}
