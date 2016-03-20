from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

def reverse_linked_list_iterative(ll):
	head = ll.first_node
	if head is None or head.next_node is None:
		return ll
	prior = head
	cur_node = head.next_node
	head.next_node = None
	while cur_node.next_node is not None:
	    next_node = cur_node.next_node
	    cur_node.next_node = prior
	    prior = cur_node
	    cur_node = next_node
	cur_node.next_node = prior
	ll.first_node = cur_node
	return ll

def reverse_linked_list_recursive(ll):
	pass




# Tests

def test_reverse_linked_list_iterative():
	inputlist = build_ll_from_lst([1,2,3])
	answerlist = build_ll_from_lst([3,2,1])
	outputlist = reverse_linked_list_iterative(inputlist)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_ll_from_lst([1])
	answerlist = build_ll_from_lst([1])
	outputlist = reverse_linked_list_iterative(inputlist)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_ll_from_lst([])
	answerlist = build_ll_from_lst([])
	outputlist = reverse_linked_list_iterative(inputlist)
	assert answerlist.lists_eq(outputlist)


if __name__ == "__main__":
	test_reverse_linked_list_iterative()
