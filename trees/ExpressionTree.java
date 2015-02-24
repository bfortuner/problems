package trees;

import java.util.*;

public class ExpressionTree<T> {

    private final String OPERATORS = "+-/*";
    private static class Node<T> {
	T val;
	Node left;
	Node right;
	public Node (T value) {
	    this.val = value;
	}
    }
    
    public static void main(String[] args) {
	ExpressionTree<String> exp = new ExpressionTree();
	String i1 = "7 3 + 2 *";
	Node<String> t1 = exp.buildTreeFromPostfix(i1);
	String postfix1 = exp.getPostfixFromTree(t1);
	System.out.println(postfix1.equals("73+2*"));
	String infix1 = exp.getInfixFromTree(t1);
	System.out.println("7+3*2".equals(infix1));
    }

    public Node<String> buildTreeFromPostfix(String postfix) {
	Stack<Node<String>> stack = new Stack();
	String[] arr = postfix.split(" ");
	for (String s : arr) {
	    Node<String> cur = new Node(s);
	    if (OPERATORS.contains(s)) {
		cur.right = stack.pop();
		cur.left = stack.pop();
	    }
	    stack.push(cur);
	}
	return stack.pop();
    }

    public String getPostfixFromTree(Node<String> node) {
	if (OPERATORS.contains(node.val)) {
	    return getPostfixFromTree(node.left) + getPostfixFromTree(node.right) + node.val;
	}
	return node.val;
    }

    public String getInfixFromTree(Node<String> node) {
	if (OPERATORS.contains(node.val)) {
	    return getInfixFromTree(node.left) + node.val + getInfixFromTree(node.right);
	}
	return node.val;
    }

    public void printTree(Node<T> tree) {
	if (tree != null) {
	    printTree(tree.left);
	    printTree(tree.right);
	    System.out.print(tree.val);
	}
    }

}
