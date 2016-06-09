from Node import Node

import sys
from Node import Node
import test_data

## Time/Space Complexity
## O(n)/O(n)

def get_height_recursive(tree):
    if tree == None:
        return 0
    left = get_height_recursive(tree.left)
    right = get_height_recursive(tree.right)
    return 1 + max(left, right)

## Level Order
def get_height_iterative(tree):
    if tree == None:
        return 0
    level = 0
    cur = []
    next = []
    cur.append(tree)
    while len(cur) > 0 or len(next) > 0:
        if len(cur) == 0:
            cur = next
            next = []
            level+=1
        else:
            node = cur.pop(0)
            if node.left != None:
                next.append(node.left)
            if node.right != None:
                next.append(node.right)
    return level+1

## Level Order - Store [Node, Level]
def get_height_iterative_dual_objs(tree):
    if tree == None:
        return 0
    level = 0
    queue = []
    queue.append([tree,1])
    while len(queue) > 0:
        nodeobj = queue.pop(0)
        if nodeobj[0].left != None:
            queue.append([nodeobj[0].left,nodeobj[1]+1])            
        if nodeobj[0].right != None:
            queue.append([nodeobj[0].right,nodeobj[1]+1])
    return nodeobj[1]

## Tests
print "RECURSIVE"
print "Height= " + str(get_height_recursive(test_data.tree1))
print "Height= " + str(get_height_recursive(test_data.tree2))
print "Height= " + str(get_height_recursive(test_data.tree3))
print "Height= " + str(get_height_recursive(test_data.tree4))

print "ITERATIVE"
print "Height= " + str(get_height_iterative(test_data.tree1))
print "Height= " + str(get_height_iterative(test_data.tree2))
print "Height= " + str(get_height_iterative(test_data.tree3))
print "Height= " + str(get_height_iterative(test_data.tree4))

print "ITERATIVE DUAL OBJS"
print "Height= " + str(get_height_iterative_dual_objs(test_data.tree1))
print "Height= " + str(get_height_iterative_dual_objs(test_data.tree2))
print "Height= " + str(get_height_iterative_dual_objs(test_data.tree3))
print "Height= " + str(get_height_iterative_dual_objs(test_data.tree4))

