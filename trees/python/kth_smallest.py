import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

def kth_smallest(root, k):
    stack = []
    node = root
    while len(stack) > 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if k == 1:
                return node.data
            k-=1
            node = node.right
    return None


##Tests
print kth_smallest(test_data.bst1,1)
print kth_smallest(test_data.bst1,2)
print kth_smallest(test_data.bst1,3)
print kth_smallest(test_data.bst1,4)
print kth_smallest(test_data.bst1,5)
print kth_smallest(test_data.bst1,6)
print kth_smallest(test_data.bst1,7)
print kth_smallest(test_data.bst1,8)

