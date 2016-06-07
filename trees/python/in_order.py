from Node import Node
import test_data

def in_order_iterative(root):
    stack = []
    node = root
    while len(stack) > 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node.data
            node = node.right
    print "complete!"
    
def in_order_recursive(root):
    if root == None:
        return None
    in_order_recursive(root.left)
    print root.data,
    in_order_recursive(root.right)
    
def in_order_search(root, target):
    if root == None:
        return None
    left = in_order_search(root.left, target)
    if left != None:
        return left
    if root.data == target:
        return root
    right = in_order_search(root.right, target)
    if right != None:
        return right
    return None



## Tests ##

l3 = Node(7)
l4 = Node(5)
r3 = Node(6)

l2 = Node(4,l3)

l1 = Node(2,l2)
r1 = Node(3,l4,r3)

root = Node(1,l1,r1)

def test_in_order_iterative():
    in_order_iterative(test_data.tree1)
    in_order_iterative(test_data.tree2)
    in_order_iterative(test_data.tree3)
    in_order_iterative(test_data.tree4)
    
def test_in_order_recursive():
    in_order_recursive(test_data.tree1)
    in_order_recursive(test_data.tree2)
    in_order_recursive(test_data.tree3)
    in_order_recursive(test_data.tree4)

def test_in_order_search():
    assert in_order_search(root, 5) == l4
    assert in_order_search(root, 4) == l2
    assert in_order_search(root, 6) == r3

test_in_order_iterative()
test_in_order_recursive()
test_in_order_search()
