import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

def is_bst(root, min, max):
    if root == None:
        return True
    if root.data < min:
        return False
    if root.data > max:
        return False
    left = is_bst(root.left, min, root.data)
    right = is_bst(root.right, root.data, max)
    return left and right

"""
In Order Traversal of BST
-This gives you a sorted list
-So check if values Out of Order!
"""

def is_bst_in_order(root):
    global prev
    if root == None:
        return True
    left = is_bst_in_order(root.left)
    if not left:
        return False
    if root.data < prev:
        return False
    prev = root.data
    return is_bst_in_order(root.right)


## TESTS -------
    
print "BINARY SEARCH TREE"
assert is_bst(test_data.bst1,-sys.maxint,sys.maxint) == True
assert is_bst(test_data.tree3,-sys.maxint,sys.maxint) == True #Skew tree

print "NOT BINARY SEARCH TREE"
assert is_bst(test_data.tree1,-sys.maxint,sys.maxint) == False
assert is_bst(test_data.tree2,-sys.maxint,sys.maxint) == False

print "IN ORDER IMPL-------"

print "BINARY SEARCH TREE"
prev = -sys.maxint
assert is_bst_in_order(test_data.bst1) == True
prev = -sys.maxint
assert is_bst_in_order(test_data.tree3) == True #Skew tree

print "NOT BINARY SEARCH TREE"
prev = -sys.maxint
assert is_bst_in_order(test_data.tree1) == False
prev = -sys.maxint
assert is_bst_in_order(test_data.tree2) == False


