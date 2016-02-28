import sys
from Node import Node
from LinkedList import LinkedList, build_ll_from_lst

def get_max_value_in_list_iterative(node):
	max_val = node.get_value()
	while node != None:
		if node.get_value() > max_val:
			max_val = node.get_value()
		node = node.get_next_node()
	return max_val

def get_max_value_in_list_recursive(node):
	if node == None:
		return -sys.maxint
	else:
		return max(node.get_value(), get_max_value_in_list_recursive(
			node.get_next_node()))



# Tests

def test_get_max_value_in_list_iterative():
	l1 = build_ll_from_lst([1,2,3])
	node = l1.get_first_node()
	assert get_max_value_in_list_iterative(node) == 3

	l1 = build_ll_from_lst([1])
	node = l1.get_first_node()
	assert get_max_value_in_list_iterative(node) == 1

	l1 = build_ll_from_lst([1,3])
	node = l1.get_first_node().get_next_node()
	assert get_max_value_in_list_iterative(node) == 3

def test_get_max_value_in_list_recursive():
	l1 = build_ll_from_lst([1,2,3])
	node = l1.get_first_node()
	assert get_max_value_in_list_recursive(node) == 3

	l1 = build_ll_from_lst([1])
	node = l1.get_first_node()
	assert get_max_value_in_list_recursive(node) == 1

	l1 = build_ll_from_lst([1,3])
	node = l1.get_first_node().get_next_node()
	assert get_max_value_in_list_recursive(node) == 3


if __name__ == "__main__":
	print "Running linked_list_basic tests!"
	test_get_max_value_in_list_iterative()
	test_get_max_value_in_list_recursive()
	print "Completed linked_list_basic tests!"
