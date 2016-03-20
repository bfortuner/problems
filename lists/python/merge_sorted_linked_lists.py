from Node import Node
from LinkedList import *

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, value=None, next_node=None):
       self.value = value
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def merge_lists_using_new_list(headA, headB):
    start_node = Node("start")
    cur_node = start_node
    while headA is not None:
        if headB is None or headA.value < headB.value:
            value = headA.value
            headA = headA.next_node
        else:
            value = headB.value
            headB = headB.next_node
        new_node = Node(value)
        cur_node.next_node = new_node
        cur_node = new_node
    while headB is not None:
        new_node = Node(headB.value)
        cur_node.next_node = new_node
        cur_node = new_node
        headB = headB.next_node
    
    return LinkedList(start_node.next_node)


def merge_lists_in_place(headA, headB):
	if headA is None:
		return LinkedList(headB)
	elif headB is None:
		return LinkedList(headA)
	elif headA.value < headB.value:
		start_node = headA
		cur_node = headA
		headA = headA.next_node
	else:
		start_node = headB
		cur_node = headB
		headB = headB.next_node
	while headA is not None:
		if headB is None or headA.value < headB.value:
			cur_node.next_node = headA
			cur_node = headA
			headA = headA.next_node
		else:
			cur_node.next_node = headB
			cur_node = headB
			headB = headB.next_node
	while headB is not None:
		cur_node.next_node = headB
		cur_node = headB
		headB = headB.next_node
	return LinkedList(start_node)



# Tests

def build_ll_from_lst(lst):
	ll = LinkedList()
	if len(lst) == 0:
		return ll
	ll.set_first_node(Node(lst[0]))
	node = ll.get_first_node()
	i = 1
	while i < len(lst):
		new_node = Node(lst[i])
		node.set_next_node(new_node)
		node = new_node
		i += 1
	return ll

def test_merge_lists_using_new_list():
	llA = build_ll_from_lst([1,3,5])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node

	mergedList = merge_lists_using_new_list(headA, headB)
	answerList = build_ll_from_lst([1,2,3,4,5])
	assert answerList.lists_eq(mergedList)

def test_merge_lists_in_place():
	llA = build_ll_from_lst([1,3,5])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node

	mergedList = merge_lists_in_place(headA, headB)
	answerList = build_ll_from_lst([1,2,3,4,5])
	assert answerList.lists_eq(mergedList)

	llC = build_ll_from_lst([1,4,5])
	llD = build_ll_from_lst([2,3])
	headC = llC.first_node
	headD = llD.first_node

	mergedList2 = merge_lists_in_place(headC, headD)
	answerList2 = build_ll_from_lst([1,2,3,4,5])
	assert answerList2.lists_eq(mergedList2)

def test_merge_lists_in_place__edge_cases():
	#List A is None
	llA = build_ll_from_lst([])
	llB = build_ll_from_lst([2,4])
	headA = llA.first_node
	headB = llB.first_node

	mergedList = merge_lists_in_place(headA, headB)
	answerList = build_ll_from_lst([2,4])
	assert answerList.lists_eq(mergedList)

	#List B is longer
	llA = build_ll_from_lst([2,4])
	llB = build_ll_from_lst([2,3,5])
	headA = llA.first_node
	headB = llB.first_node

	mergedList = merge_lists_in_place(headA, headB)
	answerList = build_ll_from_lst([2,2,3,4,5])
	assert answerList.lists_eq(mergedList)

if __name__ == "__main__":
	test_merge_lists_using_new_list()
	test_merge_lists_in_place()
  	test_merge_lists_in_place__edge_cases()
  
  
  
  
  
  
  
