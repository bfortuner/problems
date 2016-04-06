from Stack import Stack

"""
Evaluate Expression

Evaluate a space delimited mathematical that includes parentheses
expression. e.g. "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )" 
== 101

Approaches:
1) Use two stacks, one for operators, one for operands. 
If you get to close paren?, then pop last two operands off 
and combine using last operator. Pop operator and continue.
At end of string, pop result of operands

Questions:
1) Supported operators?
2) Always balanced parenthesese + equations? 
3) Empty or one element equations?
4) Integers only?

Examples:
(1 + 1)

2    
___ ___


(1 + (2 * 5) + 3)


14  
___ ___


( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )

101
___ ___

"""

def evaluate_exp(exp):
	SUPPORTED_OPERATORS = "+*-//"
	OPERANDS_REGEX = "" #For now we assume if NOT operator, then operand
	operators_stack = Stack()
	operands_stack = Stack()
	exp_list = exp.split() #splits by space default
	for char in exp_list:
		if char in SUPPORTED_OPERATORS:
			operators_stack.push(char)
		elif char == ")":
			right_operand = operands_stack.pop()
			left_operand = operands_stack.pop()
			operator = operators_stack.pop()
			operands_stack.push(math_mapper(operator, left_operand, right_operand))
		elif char == "(":
			continue #do nothing	
		else:
			operands_stack.push(int(char)) #assume operand, convert to int

	#return final remaining on operands stack
	return operands_stack.pop()


def math_mapper(operator, left_operand, right_operand):
	if operator == "+":
		return left_operand + right_operand
	elif operator == "-":
		return left_operand - right_operand
	elif operator == "*":
		return left_operand * right_operand
	elif operator == "/":
		return left_operand / right_operand
	elif operator == "//":
		return left_operand // right_operand
	elif operator is None: #Only one value left, return right operand
		return right_operand
	else:
		raise Exception("Unknown operator "  + operator)





# Tests

def test_evaluate_exp():
	exp1 = "( 1 )"
	exp2 = "( 1 + 1 )"
	exp3 = "( ( 1 + ( 2 * 5 ) ) + 3 )"
	exp4 = "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"
	exp5 = "( ( 1 + ( 2 * 5 ) ) - 3 )"
	exp6 = "( ( 1 - ( 10 / 5 ) ) * ( 3 + 6 ) )"
	assert evaluate_exp(exp1) == 1
	assert evaluate_exp(exp2) == 2
	assert evaluate_exp(exp3) == 14
	assert evaluate_exp(exp4) == 101
	assert evaluate_exp(exp5) == 8
	assert evaluate_exp(exp6) == -9

if __name__ == "__main__":
	test_evaluate_exp()
