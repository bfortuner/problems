from Node import Node
import test_data

def post_order_iterative(root):
    if root == None:
        return
    stack = []
    prev = None
    node = root
    while len(stack) > 0 or prev == None or node.left == prev:
        if node.left != None and is_child(node, prev):
            stack.append(node)
            prev = node
            node = node.left
        elif node.right != None and (is_child(node, prev) \
                                     or prev == node.left):
            stack.append(node)
            prev = node
            node = node.right
        else:
            print node.data,
            prev = node
            node = stack.pop()
    print node.data,

def is_child(node, prev):
    if prev is None:
        return True
    return node in [prev.left, prev.right]
    
def post_order_recursive(root):
    if root == None:
        return None
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print root.data,



## Tests ##

def test_post_order_iterative():
    print "Iterative---"
    print "Tree 1"
    post_order_iterative(test_data.tree1)
    print "\nTree 2"
    post_order_iterative(test_data.tree2)
    print "\nTree 3"
    post_order_iterative(test_data.tree3)

def test_post_order_recursive():
    print "\nRecursive---"
    print "Tree 1"
    post_order_recursive(test_data.tree1)
    print "\nTree 2"
    post_order_recursive(test_data.tree2)
    print "\nTree 3"
    post_order_recursive(test_data.tree3)

test_post_order_iterative()
test_post_order_recursive()
