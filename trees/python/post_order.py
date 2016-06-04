from Node import Node

def post_order(root):
    pass

def post_order_iterative(root):
    if root == None:
        return
    stack = []
    node = root
    while len(stack) > 0 or node != None:
        if node.left == None and node.right == None:
            node = bubble_up(node, stack)
        elif node.left == None:
            stack.append(node)
            node = node.right
        else:
            stack.append(node)
            node = node.left

def bubble_up(node, stack):
    parent = stack.pop()
    if parent.left is node:
        while len(stack) > 0 and parent.right == None:
            print node.data,
            node = parent
            parent = stack.pop()
        print node.data,
        node = parent.right
        stack.append(parent)
    else:
        while len(stack) > 0 and parent.right is node:
            print node.data,
            node = parent
            parent = stack.pop()
        print node.data,
        if len(stack) == 0 and parent.right is node:
            print parent.data,
            node = None
        else:
            node = parent.right
            stack.append(parent)
    return node
    
def post_order_recursive(root):
    if root == None:
        return None
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print root.data,



## Tests ##

## Tree 1
l5 = Node(5)
l3 = Node(7)
l4 = Node(6)
r3 = Node(8)

l2 = Node(4,None,l3)

l1 = Node(2,l2,l5)
r1 = Node(3,l4,r3)
root = Node(1,l1,r1)


## Tree 2
right3b = Node(7)
right3a = Node(6)
right2 = Node(3, right3a, right3b)
left3b = Node(5)
left3a = Node(4)
left2 = Node(2,left3a,left3b)
root2 = Node(1,left2,right2)

def test_post_order_iterative():
    print "Iterative---"
    print "Tree 1"
    post_order_iterative(root)
    print "\nTree 2"
    post_order_iterative(root2)

def test_post_order_recursive():
    print "\nRecursive---"
    print "Tree 1"
    post_order_recursive(root)
    print "\nTree 2"
    post_order_recursive(root2)

test_post_order_iterative()
test_post_order_recursive()
