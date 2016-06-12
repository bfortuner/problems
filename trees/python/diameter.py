import sys
from Node import Node
import test_data

## Time/Space Complexity
#O(n), O(n)

"""
Approaches
1) Post Order w Hashmap
   O(n), O(n^height)
2) Level Order w Two Queues
"""

def diameter(tree):
    if tree == None:
        return 0
    diameter = level_map(tree, 0)
    return max(diameter.values())
    
def level_map(tree, level):
    if tree == None:
        return {}
    left = level_map(tree.left, level+1)
    right = level_map(tree.right, level+1)
    map = join(left, right)
    map[level] = 1
    return map

def join(map1, map2):
    for key2 in map2:
        if key2 in map1:
            map1[key2] += map2[key2]
        else:
            map1[key2] = map2[key2]
    return map1

print diameter(test_data.tree1)
print diameter(test_data.tree2)
print diameter(test_data.tree3)
print diameter(test_data.tree4)
