from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node



def remove_duplicates_sorted(head):
	start = head
	while head is not None:
		while head.next is not None and \
		head.value == head.next.value:
			head.next = head.next.next
		head = head.next
	return LinkedList(start)

def remove_duplicates_unsorted(head):
	if head is None:
		return LinkedList(head)
	hashmap = {}
	hashmap[head.value] = 1
	prior = head
	cur = head.next
	while cur is not None:
		if hashmap.get(cur.value) is not None:
			prior.next = cur.next
		else:
			hashmap[cur.value] = 1
			prior = cur
		cur = cur.next
	return LinkedList(head)



#Tests

def test_remove_duplicates_sorted():
	l1 = build_ll_from_lst([1,2,2,3,3,4])
	l2 = build_ll_from_lst([1,1,1,1,1,1,1])
	l3 = build_ll_from_lst([2,3,3,4,6])
	l4 = build_ll_from_lst([10])

	a1 = build_ll_from_lst([1,2,3,4])
	a2 = build_ll_from_lst([1])
	a3 = build_ll_from_lst([2,3,4,6])
	a4 = build_ll_from_lst([10])

	assert remove_duplicates_sorted(l1.head).lists_eq(a1)
	assert remove_duplicates_sorted(l2.head).lists_eq(a2)
	assert remove_duplicates_sorted(l3.head).lists_eq(a3)
	assert remove_duplicates_sorted(l4.head).lists_eq(a4)

def test_remove_duplicates_unsorted():
	l1 = build_ll_from_lst([1,2,4,2,1,3,7,3,4])
	l2 = build_ll_from_lst([1,1,1,1,1,1,1])
	l3 = build_ll_from_lst([6,2,4,3,3,4,6])
	l4 = build_ll_from_lst([10])

	a1 = build_ll_from_lst([1,2,4,3,7])
	a2 = build_ll_from_lst([1])
	a3 = build_ll_from_lst([6,2,4,3])
	a4 = build_ll_from_lst([10])

	assert remove_duplicates_unsorted(l1.head).lists_eq(a1)
	assert remove_duplicates_unsorted(l2.head).lists_eq(a2)
	assert remove_duplicates_unsorted(l3.head).lists_eq(a3)
	assert remove_duplicates_unsorted(l4.head).lists_eq(a4)

if __name__ == "__main__":
	test_remove_duplicates_sorted()
	test_remove_duplicates_unsorted()
