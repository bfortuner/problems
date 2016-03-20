from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

def compare_lists_recursive(headA, headB):
    if headA == None and headB == None:
        return True
    elif headA is None or headB is None:
        return False
    elif headA.value != headB.value:
        return False
    return compare_lists_recursive(headA.next_node, headB.next_node)

def compare_lists_iterative(headA, headB):
	while headA is not None:
		if headB is None or headB.value != headA.value:
			return False
		headA = headA.next_node
		headB = headB.next_node
	return headB is None



#Tests

def test_compare_lists_recursive():
	llA = build_ll_from_lst([2,4])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node
	assert compare_lists_recursive(headA, headB)

	llA = build_ll_from_lst([2])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node
	assert not compare_lists_recursive(headA, headB)

def test_compare_lists_iterative():
	llA = build_ll_from_lst([2,4])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node
	assert compare_lists_iterative(headA, headB)

	llA = build_ll_from_lst([2])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node
	assert not compare_lists_iterative(headA, headB)


if __name__ == "__main__":
	test_compare_lists_recursive()
	test_compare_lists_iterative()

