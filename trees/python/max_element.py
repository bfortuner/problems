import sys
from Node import Node
import test_data

## Time/Space Complexity
O(n), O(n)

## Post Order
def max_element(tree):
    if tree == None:
        return -sys.maxint
    left_max = max_element(tree.left)
    right_max = max_element(tree.right)
    return max(left_max, right_max, tree.data)

## Pre Order
def max_element_iterative(tree):
    max_element = -sys.maxint
    if tree == None:
        return
    stack = []
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node.data > max_element:
            max_element = node.data
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return max_element

print max_element(test_data.tree1)
print max_element(test_data.tree2)
print max_element(test_data.tree3)

print "ITERATIVE"
print max_element_iterative(test_data.tree1)
print max_element_iterative(test_data.tree2)
print max_element_iterative(test_data.tree3)
