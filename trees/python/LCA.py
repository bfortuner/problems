import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

def LCA(root, a, b):
    if root == None:
        return None
    left = LCA(root.left, a, b)
    right = LCA(root.right, a, b)
    if left != None and right != None:
        return root
    if root is a or root is b:
        return root
    if left != None:
        return left
    if right != None:
        return right
    return None

"""
Binary Search Tree

Cases:
1) Both left (both smaller than root)
2) Both right (both greater than root)
3) Root is LCA (one smaller, one greater)
"""

def LCA_BST(root, a, b):
    if root == None:
        return None
    if (root.data >= a.data and root.data <= b.data):
        return root
    if (root.data <= a.data and root.data >= b.data):
        return root
    if root.data > a.data and root.data > b.data:
        return LCA_BST(root.left, a, b)
    else:
        return LCA_BST(root.right, a, b)


## TESTS -------
    
## Tree 1
l5 = Node(5)
l3 = Node(7)
l4 = Node(6)
r3 = Node(8)
l2 = Node(4,None,l3)
l1 = Node(2,l2,l5)
r1 = Node(3,l4,r3)
tree1 = Node(1,l1,r1)

print "BINARY TREE"
assert LCA(tree1, l4, r3).data == 3
assert LCA(tree1, l1, r3).data == 1
assert LCA(tree1, l1, l2).data == 2
assert LCA(tree1, tree1, r1).data == 1

## BST 1
l6 = Node(12)
l5 = Node(6)
l4 = Node(9)
r3 = Node(15,l6)
l2 = Node(3)
l1 = Node(4,l2,l5)
r1 = Node(11,l4,r3)
bst1 = Node(7,l1,r1)

print "BINARY SEARCH TREE"
assert LCA_BST(bst1, l1, r3).data == 7
assert LCA_BST(bst1, l4, r3).data == 11
assert LCA_BST(bst1, l2, l5).data == 4
assert LCA_BST(bst1, r1, r3).data == 11
