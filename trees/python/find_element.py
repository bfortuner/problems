import sys
from Node import Node
import test_data

## Time/Space Complexity
## O(n)/O(n)

## In Order
def find_element(tree, value):
    if tree == None:
        return False
    left = find_element(tree.left, value)
    if left == True:
        return True
    if tree.data == value:
        return True
    return find_element(tree.right, value)

## In Order
def find_element_iterative(tree, value):
    if tree == None:
        return False
    stack = []
    node = tree
    while len(stack) > 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.data == value:
                return True
            node = node.right
    return False
    
print find_element(test_data.tree1, 8)
print find_element(test_data.tree2, 7)
print find_element(test_data.tree3, 0)
print find_element(test_data.tree4, 3)

print "ITERATIVE"
print find_element_iterative(test_data.tree1, 8)
print find_element_iterative(test_data.tree2, 7)
print find_element_iterative(test_data.tree3, 0)
print find_element_iterative(test_data.tree4, 3)
