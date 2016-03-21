from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node


"""
Insert Node at Nth Position in LinkedList

You're given the pointer to the head node of a linked list, 
an integer to add to the list and the position at which the 
integer must be inserted. Create a new node with the given integer, 
insert this node at the desired position and return the head node. 
A position of 0 indicates head, a position of 1 indicates one node 
away from the head and so on.
"""

def insert_nth(head, val, position):
	"""
	Insert value at position N in list
	pos = 0 == head
	"""
	if head is None or position == 0:
	    return LinkedList(Node(val, head))
	i = 1
	prior_node = head
	cur_node = head.next
	while i < position:
	    prior_node = cur_node
	    cur_node = cur_node.next
	    i+=1
	new_node = Node(val, cur_node)
	prior_node.next = new_node
	return LinkedList(head)



# Tests

def test_insert_nth():
	inputlist = build_ll_from_lst([1,2,4])
	answerlist = build_ll_from_lst([1,2,3,4])
	outputlist = insert_nth(inputlist.head, 3,2)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_ll_from_lst([1,2,4])
	answerlist = build_ll_from_lst([0,1,2,4])
	outputlist = insert_nth(inputlist.head, 0,0)
	assert answerlist.lists_eq(outputlist)

if __name__ == "__main__":
	test_insert_nth()