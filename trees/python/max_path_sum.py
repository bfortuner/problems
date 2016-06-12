import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

"""
Approaches
"""

def max_path_sum(tree):
    if tree == None:
        return 0
    return get_max(tree)[1]
    
def get_max(root):
    if root == None:
        return [0,-sys.maxint]
    left = get_max(root.left)
    right = get_max(root.right)
    cur_max = max(root.data,left[1],right[1],
                  root.data+left[0],root.data+right[0])
    cur_sum = root.data
    if left[0] > 0 and left[0] > right[0]:
        cur_sum += left[0]
    elif right[0] > 0:
        cur_sum += right[0]
    return [cur_sum,cur_max]
        

print max_path_sum(test_data.tree1)
print max_path_sum(test_data.tree2)
print max_path_sum(test_data.tree3)
print max_path_sum(test_data.tree4)
print max_path_sum(test_data.negatives)
