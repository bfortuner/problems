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


if __name__ == "__main__":
	test_get_max_value_in_list_iterative()
	test_get_max_value_in_list_recursive()
