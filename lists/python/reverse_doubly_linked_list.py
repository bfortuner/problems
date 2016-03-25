from LinkedList import LinkedList
from LinkedList import build_doubly_ll_from_lst
from DoublyNode import DoublyNode


"""
Reverse a doubly linked list

The head node might be NULL to indicate that the list is empty.
-----------
None <- A <-> B <-> C -> None

None <- C <-> B <-> A -> None

      p    c   n
1 <-> 2 -> None

2 <-> 1 -> None
"""

def reverse_doubly_ll(ll):
	if ll.head is None or ll.head.next is None:
		return ll
	cur_node = ll.head
	while cur_node is not None:
		prev_node = cur_node
		next_node = cur_node.next
		cur_node.next = cur_node.prev
		cur_node.prev = cur_node.next
		cur_node = next_node
	return LinkedList(prev_node)




# Tests

def test_reverse_doubly_ll():
	inputlist = build_doubly_ll_from_lst([])
	answerlist = build_doubly_ll_from_lst([])
	outputlist = reverse_doubly_ll(inputlist)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_doubly_ll_from_lst([1])
	answerlist = build_doubly_ll_from_lst([1])
	outputlist = reverse_doubly_ll(inputlist)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_doubly_ll_from_lst([1,2,4])
	answerlist = build_doubly_ll_from_lst([4,2,1])
	outputlist = reverse_doubly_ll(inputlist)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_doubly_ll_from_lst([1,2])
	answerlist = build_doubly_ll_from_lst([2,1])
	outputlist = reverse_doubly_ll(inputlist)
	assert answerlist.lists_eq(outputlist)

	inputlist = build_doubly_ll_from_lst([1,1,1])
	answerlist = build_doubly_ll_from_lst([1,1,1])
	outputlist = reverse_doubly_ll(inputlist)
	assert answerlist.lists_eq(outputlist)

if __name__ == "__main__":
	test_reverse_doubly_ll()