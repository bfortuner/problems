from LinkedList import LinkedList
from LinkedList import build_doubly_ll_from_lst
from DoublyNode import DoublyNode


"""
Insert node into a sorted doubly linked list

You're given the pointer to the head node of a sorted doubly 
linked list and an integer to insert into the list. Create a node 
and insert it into the appropriate position in the list. 
The head node might be NULL to indicate that the list is empty.
"""


def insert_node_into_sorted_doubly_ll(ll, new_node):
	if ll.head is None:
		return LinkedList(new_node)
	prev_node = ll.head
	cur_node = ll.head.next
	while cur_node is not None:
		if new_node.value <= cur_node.value:
			prev_node.next = new_node
			new_node.next = cur_node
			new_node.prev = prev_node
			cur_node.prev = new_node
			return ll
		prev_node = cur_node
		cur_node = cur_node.next
	prev_node.next = new_node
	new_node.prev = prev_node
	return ll



# Tests

def test_insert_node_into_sorted_doubly_ll():
	inputlist = build_doubly_ll_from_lst([])
	answerlist = build_doubly_ll_from_lst([1])
	outputlist = insert_node_into_sorted_doubly_ll(inputlist, DoublyNode(1))
	assert answerlist.lists_eq(outputlist)

	inputlist = build_doubly_ll_from_lst([1,2,4])
	answerlist = build_doubly_ll_from_lst([1,2,3,4])
	outputlist = insert_node_into_sorted_doubly_ll(inputlist,DoublyNode(3))
	assert answerlist.lists_eq(outputlist)

	inputlist = build_doubly_ll_from_lst([1,2,4])
	answerlist = build_doubly_ll_from_lst([1,2,4,6])
	outputlist = insert_node_into_sorted_doubly_ll(inputlist,DoublyNode(6))
	assert answerlist.lists_eq(outputlist)

if __name__ == "__main__":
	test_insert_node_into_sorted_doubly_ll()