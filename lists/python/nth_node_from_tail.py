from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

"""
Return data in Nth node from the end
head could be None as well for empty list

# Approaches
1) Use a queue to keek track of last pos_from_tail values, then dequeue at end
2) Use list, then return list[len(list)-pos_from_tail]
3) Two loops. Find length, then stop when you get to Node (if you can't use data structure)
"""

def get_nth_node_from_tail(node, pos_from_tail):
	if node is None:
		return None
	vals_list = []
	while node is not None:
		vals_list.append(node.value)
		node = node.next
	return vals_list[len(vals_list) - pos_from_tail - 1]



# Tests

def test_get_nth_node_from_tail():
	l1 = build_ll_from_lst([1,2,3])
	node = l1.head
	assert get_nth_node_from_tail(node,0) == 3
	assert get_nth_node_from_tail(node,1) == 2
	assert get_nth_node_from_tail(node,2) == 1

if __name__ == "__main__":
	test_get_nth_node_from_tail()