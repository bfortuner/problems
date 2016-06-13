import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

"""
Approaches
1) Post Order w Hashmap
   O(n), O(n + ~height)
2) Level Order w Two Queues
"""

def zigzag(root):
    if root == None:
        return
    print root.data,
    right = []
    left = []
    primary = right
    secondary = left
    right.append(root)
    while len(left) > 0 or len(right) > 0:
        if len(primary) == 0:
            if primary == right:
                for i in range(len(left)-1,-1,-1):
                    print left[i].data,
                primary = left
                secondary = right
            else:
                for i in range(len(right)):
                    print right[i].data,
                primary = right
                secondary = left
        node = primary.pop(0)
        if node.left != None:
            secondary.append(node.left)
        if node.right != None:
            secondary.append(node.right)
    print

zigzag(test_data.tree1)
zigzag(test_data.tree2)
zigzag(test_data.tree3)
zigzag(test_data.tree4)
