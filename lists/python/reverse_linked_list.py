from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

def reverse_linked_list_iterative(ll):
	head = ll.head
	if head is None or head.next is None:
		return ll
	prior = head
	cur_node = head.next
	head.next = None
	while cur_node.next is not None:
	    next = cur_node.next
	    cur_node.next = prior
	    prior = cur_node
	    cur_node = next
	cur_node.next = prior
	ll.head = cur_node
	return ll

def reverse_linked_list_recursive(cur_node, prior_node):
	if cur_node is None:
		return prior_node
	next = cur_node.next
	cur_node.next = prior_node
	return reverse_linked_list_recursive(next, cur_node)
	


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

def test_reverse_linked_list_recursive():
	inputlist = build_ll_from_lst([1,2,3])
	head1 = inputlist.head
	outputnode = reverse_linked_list_recursive(head1, None)
	assert outputnode.value == 3
	outputnode = outputnode.next
	assert outputnode.value == 2
	outputnode = outputnode.next
	assert outputnode.value == 1
	outputnode = outputnode.next
	assert outputnode is None

	inputlist = build_ll_from_lst([1])
	head1 = inputlist.head
	outputnode = reverse_linked_list_recursive(head1, None)
	assert outputnode.value == 1
	outputnode = outputnode.next
	assert outputnode is None

if __name__ == "__main__":
	test_reverse_linked_list_iterative()
	test_reverse_linked_list_recursive()

