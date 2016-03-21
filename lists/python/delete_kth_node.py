from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from LinkedList import get_test_linked_list
from Node import Node

"""
Delete Kth Node in LinkedList
"""

def delete_kth_node(ll, k):
	'''Delete 0th node means 1st node'''
	i = 0
	node = ll.get_first_node()
	if node is None:
		return ll
	if k == 0:
		ll.set_first_node(node.get_next_node())
		return ll
	while i < k-1 and node.get_next_node() is not None:
		node = node.get_next_node()
		i += 1
	if node.get_next_node() is not None:
		new_next_node = node.get_next_node().get_next_node()
		node.set_next_node(new_next_node)
	return ll



#Tests

def test_delete_kth_node__empty_list():
	# None -->
	empty_list = LinkedList()
	delete_kth_node(empty_list, 3)
	assert empty_list.get_first_node() is None

def test_delete_kth_node__one_element():
	# A --> None
	first_node = Node("A")
	test_list = LinkedList(first_node)
	delete_kth_node(test_list, 1)
	assert test_list.get_first_node() == first_node

	delete_kth_node(test_list, 3)
	assert test_list.get_first_node() == first_node

	delete_kth_node(test_list, 0)
	assert test_list.get_first_node() == None	

def test_delete_kth_node__three_elements():
	# A --> B --> C --> None
	test_list = get_test_linked_list()
	delete_kth_node(test_list,4)
	delete_kth_node(test_list,3)
	delete_kth_node(test_list,1)
	delete_kth_node(test_list,0)
	assert test_list.get_first_node().get_value() == "C"


if __name__ == "__main__":
	test_delete_kth_node__empty_list()
	test_delete_kth_node__one_element()
	test_delete_kth_node__three_elements()
