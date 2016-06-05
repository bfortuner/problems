from Node import Node

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

##Skewed Tree
ra4 = Node(5,None,None)
ra3 = Node(4,None,ra4)
ra2 = Node(3,None,ra3)
ra1 = Node(2,None,ra2)
root3 = Node(1,None,ra1)

##Trees
tree1 = root
tree2 = root2
tree3 = root3
