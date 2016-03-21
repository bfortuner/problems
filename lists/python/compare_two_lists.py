from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

"""
Return True if Each Lists Contains 
The Same Values in the Same Order
"""

def compare_lists_recursive(headA, headB):
    if headA == None and headB == None:
        return True
    elif headA is None or headB is None:
        return False
    elif headA.value != headB.value:
        return False
    return compare_lists_recursive(headA.next, headB.next)

def compare_lists_iterative(headA, headB):
	while headA is not None:
		if headB is None or headB.value != headA.value:
			return False
		headA = headA.next
		headB = headB.next
	return headB is None



#Tests

def test_compare_lists_recursive():
	llA = build_ll_from_lst([2,4])
	llB = build_ll_from_lst([2,4])
	headA = llA.head
	headB = llB.head
	assert compare_lists_recursive(headA, headB)

	llA = build_ll_from_lst([2])
	llB = build_ll_from_lst([2,4])
	headA = llA.head
	headB = llB.head
	assert not compare_lists_recursive(headA, headB)

def test_compare_lists_iterative():
	llA = build_ll_from_lst([2,4])
	llB = build_ll_from_lst([2,4])
	headA = llA.head
	headB = llB.head
	assert compare_lists_iterative(headA, headB)

	llA = build_ll_from_lst([2])
	llB = build_ll_from_lst([2,4])
	headA = llA.head
	headB = llB.head
	assert not compare_lists_iterative(headA, headB)


if __name__ == "__main__":
	test_compare_lists_recursive()
	test_compare_lists_iterative()

