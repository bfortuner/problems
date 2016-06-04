from Node import Node

def level_order(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print node.data,
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)


## Tests ##

## Tree 1
l5 = Node(5)
l3 = Node(8)
l4 = Node(6)
r3 = Node(7)

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

def test_level_order():
    print "Iterative---"
    print "Tree 1"
    level_order(root)
    print "\nTree 2"
    level_order(root2)


test_level_order()
