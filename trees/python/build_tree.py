import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

"""
Given Pre-Order and In-Order
Traversal Lists of Nodes, 
Reconstruct a Binary Tree

Inorder: Node(D), Node(B), EAFC
Preorder: Node(A), Node(B), DECF
"""

def build_tree(po, io):
    if len(po) < 1:
        return None
    if len(po) == 1:
        return po[0]
    root = po[0]
    i = 0
    while io[i] != root:
        i+=1
    root.left = build_tree(po[1:i+1], io[:i])
    root.right = build_tree(po[i+1:], io[i+1:])
    return root


na = Node("A")
nb = Node("B")
nd = Node("D")
ne = Node("E")
nc = Node("C")
nf = Node("F")

po = [na,nb,nd,ne,nc,nf]
io = [nd,nb,ne,na,nf,nc]
tree = build_tree(po,io)
assert tree.data == "A"
assert tree.left.data == "B"
assert tree.left.left.data == "D"
assert tree.left.right.data == "E"
assert tree.right.data == "C"
assert tree.right.left.data == "F"
assert tree.right.right == None

