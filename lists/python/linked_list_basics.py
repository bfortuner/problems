import sys
from Node import Node
from LinkedList import LinkedList, build_ll_from_lst

def get_max_value_in_list_iterative(node):
	max_val = node.value
	while node != None:
		if node.value > max_val:
			max_val = node.value
		node = node.get_next()
	return max_val

def get_max_value_in_list_recursive(node):
	if node == None:
		return -sys.maxint
	else:
		return max(node.value, get_max_value_in_list_recursive(
			node.get_next()))

def get_nth_node_from_tail(node, pos_from_tail):
	"""
	Get Node data of the Nth Node from the end.
 	head could be None as well for empty list
	"""
	# Use a queue to keek track of last pos_from_tail values, then dequeue at end
	# Use list, then return list[len(list)-pos_from_tail]
	# Two loops. Find length, then stop when you get to Node (if you can't use data structure)
	if node is None:
		return None
	vals_list = []
	while node is not None:
		vals_list.append(node.value)
		node = node.next
	return vals_list[len(vals_list) - pos_from_tail - 1]



# Tests

def test_get_max_value_in_list_iterative():
	l1 = build_ll_from_lst([1,2,3])
	node = l1.head
	assert get_max_value_in_list_iterative(node) == 3

	l1 = build_ll_from_lst([1])
	node = l1.head
	assert get_max_value_in_list_iterative(node) == 1

	l1 = build_ll_from_lst([1,3])
	node = l1.head.get_next()
	assert get_max_value_in_list_iterative(node) == 3

def test_get_max_value_in_list_recursive():
	l1 = build_ll_from_lst([1,2,3])
	node = l1.head
	assert get_max_value_in_list_recursive(node) == 3

	l1 = build_ll_from_lst([1])
	node = l1.head
	assert get_max_value_in_list_recursive(node) == 1

	l1 = build_ll_from_lst([1,3])
	node = l1.head.get_next()
	assert get_max_value_in_list_recursive(node) == 3

def test_get_nth_node_from_tail():
	l1 = build_ll_from_lst([1,2,3])
	node = l1.head
	assert get_nth_node_from_tail(node,0) == 3
	assert get_nth_node_from_tail(node,1) == 2
	assert get_nth_node_from_tail(node,2) == 1

if __name__ == "__main__":
	print "Running linked_list_basic tests!"
	test_get_max_value_in_list_iterative()
	test_get_max_value_in_list_recursive()
	test_get_nth_node_from_tail()
	print "Completed linked_list_basic tests!"
