from Node import Node
import test_data

def print_upside_down(root):
    if root == None:
        return
    queue = []
    stack = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        stack.append(node)
        if node.right != None:
            queue.append(node.right)
        if node.left != None:
            queue.append(node.left)
    while len(stack) > 0:
        print(stack.pop().data),
    print "\n"

## Tests ##
print_upside_down(test_data.tree1)
print_upside_down(test_data.tree2)
print_upside_down(test_data.tree3)
print_upside_down(test_data.tree4)
