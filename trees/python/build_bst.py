import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

"""
Build BST from Sorted List
"""

def build_bst(A):
    if len(A) == 0:
        return None
    mid = len(A)/2
    root = Node(A[mid])
    root.left = build_bst(A[:mid])
    root.right = build_bst(A[mid+1:])
    return root
    
"""
Return a sorted list from BST
"""

def sorted_list_from_bst(root):
    if root == None:
        return []
    left = sorted_list_from_bst(root.left)
    result = [root.data]
    right = sorted_list_from_bst(root.right)
    return left + result + right

## TESTS -------
    
a1 = [3,4,6,7,9,11,12,15]
output = build_bst(a1)
print output.data
#LEFT
print output.left.data
print output.left.left.data
print output.left.left.left.data
#RIGHT
print output.right.data
print output.right.left.data
print output.right.right.data
assert sorted_list_from_bst(output) == a1
