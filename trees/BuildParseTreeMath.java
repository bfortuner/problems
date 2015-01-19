package trees;

public class BuildParseTreeMath {

    public static void main(String[] args) {
	String eq = "( 3 + ( 4 * 5 ) )";
	BinaryTree tree = buildParseTree(eq);
	printTree(tree);
    }

    public static BinaryTree buildParseTree(String equation) {
	String[] list = equation.split(" ");
	BinaryTree curTree = new BinaryTree(""); 
	int i = 0;
	while (i < list.length) {
	    if ( list[i].equals("(") ) {
		BinaryTree leftChild = new BinaryTree("");
		curTree.setLeftChild(leftChild);
		leftChild.setParent(curTree);
		curTree = leftChild;
	    } else if ( list[i].equals(")") ) {
		if (i != list.length - 1) {
		    curTree = curTree.getParent();
		}
	    } else if ("+-*/".contains(list[i])) {
		curTree.setValue(list[i]);
		BinaryTree rightChild = new BinaryTree("");
		curTree.setRightChild(rightChild);
		rightChild.setParent(curTree);
		curTree = rightChild;
	    } else {
		curTree.setValue(list[i]);
		curTree = curTree.getParent();
	    }
	    i++;
	}
	return curTree;
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
