from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from LinkedList import get_test_linked_list
from Node import Node

"""
Delete Kth Node in LinkedList

You're given the pointer to the head node of a linked list and
the position of a node to delete. Delete the node at the given 
position and return the head node. A position of 0 indicates head, 
a position of 1 indicates one node away from the head and so on.
"""

def delete_kth_node(ll, k):
	'''Delete 0th node means 1st node'''
	i = 0
	node = ll.head
	if node is None:
		return ll
	if k == 0:
		ll.set_head(node.get_next())
		return ll
	while i < k-1 and node.get_next() is not None:
		node = node.get_next()
		i += 1
	if node.get_next() is not None:
		new_next = node.get_next().get_next()
		node.set_next(new_next)
	return ll



#Tests

def test_delete_kth_node__empty_list():
	# None -->
	empty_list = LinkedList()
	delete_kth_node(empty_list, 3)
	assert empty_list.head is None

def test_delete_kth_node__one_element():
	# A --> None
	head = Node("A")
	test_list = LinkedList(head)
	delete_kth_node(test_list, 1)
	assert test_list.head == head

	delete_kth_node(test_list, 3)
	assert test_list.head == head

	delete_kth_node(test_list, 0)
	assert test_list.head == None	

def test_delete_kth_node__three_elements():
	# A --> B --> C --> None
	test_list = get_test_linked_list()
	delete_kth_node(test_list,4)
	delete_kth_node(test_list,3)
	delete_kth_node(test_list,1)
	delete_kth_node(test_list,0)
	assert test_list.head.value == "C"


if __name__ == "__main__":
	test_delete_kth_node__empty_list()
	test_delete_kth_node__one_element()
	test_delete_kth_node__three_elements()
