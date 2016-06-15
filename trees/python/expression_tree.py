from Node import Node

"""
Arithmetic Expression Tree

Write 3 methods:
1) Convert infix to posix expression
2) Build expression tree from postfix expression
3) Evaluate expression tree

Input: "7 + 3 * 4 - 2"
Ouput:
    (-)
    / \
  (+) (2)
  / \
(7) (*)
    / \
  (4) (3)

Approaches:
1) Loops through strings, no stacks - read expression right to left
2) Stacks (Should implement) - read expression left to right

*Try handling '(' and ')' next time!
"""

HIGHER_ORDER="*/"
LOWER_ORDER="+-"
OPERATORS=HIGHER_ORDER+LOWER_ORDER

def infix_to_postfix(infix):
    postfix = ""
    i = 0
    last = None
    while i < len(infix):
        if infix[i] not in OPERATORS:
            postfix += infix[i]
        elif infix[i] in HIGHER_ORDER:
            postfix += infix[i+1] + infix[i]
            i+=1
        elif last != None:
            postfix += last
            last = infix[i]
        else:
            last = infix[i]
        i+=1
    if last != None:
        postfix += last
    return postfix

def build_exp_tree(postfix):
    root = Node(postfix[-1])
    node = root
    i = len(postfix)-2
    while i >= 0:
        next = Node(postfix[i])
        if next.data in HIGHER_ORDER:
            if node.right == None:
                next.right = Node(postfix[i-1])
                next.left = Node(postfix[i-2])
                node.right = next
                i-=2
            else:
                node.left = next
                node = next
        else:
            if node.right == None:
                node.right = next
            else:
                node.left = next
                node = next
        i-=1
    return root
                
def evaluate(root):
    if root.data not in OPERATORS:
        return root.data
    left = evaluate(root.left)
    right = evaluate(root.right)
    return operate(left,right,root.data)

def operate(left, right, operator):
    num1 = int(left)
    num2 = int(right)
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    raise Exception("Operator Not Supported!")



## Tests
assert infix_to_postfix("A+B") == "AB+"
assert infix_to_postfix("A*B") == "AB*"
assert infix_to_postfix("A+B*C") == "ABC*+"
assert infix_to_postfix("A+B*C-D") == "ABC*+D-"
assert infix_to_postfix("A/B+C/D") == "AB/CD/+"
assert infix_to_postfix("A+B+C+D") == "AB+C+D+"
assert infix_to_postfix("A*B*C*D*E") == "AB*C*D*E*"

#Expressions
ex1 = "3+5"
ex2 = "3*5"
ex3 = "3+5*2"
ex4 = "7+3*4-2" #734*+2-
ex5 = "2*3*4*5" #23*4*5*
ex6 = "2*3+4*5" 

t1 = build_exp_tree(infix_to_postfix(ex1))
t2 = build_exp_tree(infix_to_postfix(ex2))
t3 = build_exp_tree(infix_to_postfix(ex3))
t4 = build_exp_tree(infix_to_postfix(ex4))
t5 = build_exp_tree(infix_to_postfix(ex5))
t6 = build_exp_tree(infix_to_postfix(ex6))
assert t4.data == "-"
assert t4.right.data == "2" 
assert t4.left.data == "+"
assert t4.left.left.data == "7"
assert t4.left.right.data == "*"
assert t4.left.right.left.data == "3"
assert t4.left.right.right.data == "4"

assert evaluate(t1) == 8
assert evaluate(t2) == 15
assert evaluate(t3) == 13
assert evaluate(t4) == 17
assert evaluate(t5) == 120
assert evaluate(t6) == 26

