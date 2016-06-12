import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

def LCA(root, node1, node2):
    if root == None:
        return None
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)
    if left != None and right != None:
        return root
    if root == node1 or root == node2:
        return root
    if left != None:
        return left
    if right != None:
        return right
    return None

## Tree 1
l5 = Node(5)
l3 = Node(7)
l4 = Node(6)
r3 = Node(8)
l2 = Node(4,None,l3)
l1 = Node(2,l2,l5)
r1 = Node(3,l4,r3)
tree1 = Node(1,l1,r1)

assert LCA(tree1, l4, r3).data == 3
assert LCA(tree1, l1, r3).data == 1
assert LCA(tree1, l1, l2).data == 2
