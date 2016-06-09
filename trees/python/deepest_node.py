from Node import Node
import test_data

## Time/Space Complexity
## O(n)/O(n)

## Deepest BFS
"""
Normal BFS 
Last node dequed is the deepest!
"""

def get_deepest_recursive(nodeobj):
    if nodeobj[0] == None:
        return [None,0]
    left = get_deepest_recursive([nodeobj[0].left,nodeobj[1]+1])
    right = get_deepest_recursive([nodeobj[0].right,nodeobj[1]+1])
    if left[0] == None and right[0] == None:
        return nodeobj
    if left[1] > right[1]:
        return left
    return right

## Tests
print "RECURSIVE"
print "Deepest= " + str(get_deepest_recursive([test_data.tree1,0])[0].data)
print "Deepest= " + str(get_deepest_recursive([test_data.tree2,0])[0].data)
print "Deepest= " + str(get_deepest_recursive([test_data.tree3,0])[0].data)
print "Deepest= " + str(get_deepest_recursive([test_data.tree4,0])[0].data)
