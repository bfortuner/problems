package stacks;

import java.util.Stack;

public class EvaluateExpression {

    private final String SUPPORTED_OPS = "+-*/";
    public static void main(String[] args) {
	EvaluateExpression eval = new EvaluateExpression();
	String s1 = "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )";
	System.out.println(eval.solveExp(s1) == 101);
    }

    public int solveExp(String exp) {
	Stack<Integer> operands = new Stack();
	Stack<String> operators = new Stack();
	String[] arr = exp.split(" ");
	for (String s : arr) {
	    if (s.equals("(")) {
		//skip
	    } else if (SUPPORTED_OPS.contains(s)) {
		operators.push(s);
	    } else if (s.equals(")")) {
		int b = operands.pop();
		int a = operands.pop();
		String operator = operators.pop();
		int val = calculate(operator, a, b);
		operands.push(val);
	    } else {
		int val = Integer.parseInt(s);
		operands.push(val);
	    }
	}
	return operands.pop();
    }

    private int calculate(String operator, int a, int b) {
	if (operator.equals("+")) {
	    return a + b;
	}
	if (operator.equals("-")) {
	    return a - b;
	}
	if (operator.equals("*")) {
	    return a * b;
	}
	if (operator.equals("/")) {
	    return a / b;
	}
	return -1;
    }

}
