from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

"""
Is A linked List Circular?

Return True if Linked List Contains a Cycle
Where a previous node will be visited twice

1 --> NULL

1 --> 2 --> NULL

1 --> 2
  <--
    
1 --> 2 --> 3
^           |
|           |
 -----------     
  
1 --> 2 --> 3 --> 4
      ^           |
      |           |
       -----------     
"""

def has_cycle_hashmap(head):
	hashmap = {}
	while head is not None:
		obj_hash_id = id(head)
		if hashmap.get(obj_hash_id) is not None:
			return True
		hashmap[obj_hash_id] = 1
		head = head.next
	return False

def has_cycle_runners(head):
	"""
	1) Fast runner, head.next.next
	2) Slow runner, head.next
	3) Keep going until Fast running gets to None
	OR 
	4) Fast Runner gets to Slow Runner
	"""
	slow = head
	fast = head
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

def get_first_node_in_cycle(head):
	"""
	Assumes there WILL be a cycle (no None)
	return first node in cycle
	"""
	slow = head.next
	fast = head.next.next
	while fast != slow:
		slow = slow.next
		fast = fast.next.next

	pos = 0
	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next
		pos += 1
	return pos

def find_length_of_cycle(head):
	"""
	Assumes there WILL be a cycle (no None)
	return first node in cycle
	"""
	#Confirm Loop
	slow = head.next
	fast = head.next.next
	while fast != slow:
		slow = slow.next
		fast = fast.next.next

	#Find the Start of Cyclce
	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next

	#Get Length of Cycle
	length = 0
	fast = fast.next
	while fast != slow:
		fast = fast.next
		length += 1
	return length



#Tests

def get_test_circular_ll_1():
	"""
	1 --> 2 --> 3
	^           |
	|           |
	 -----------     
	"""
	third_node = Node("C")
	second_node = Node("B", third_node)
	head = Node("A", second_node)
	third_node.next = head #cycle

	return LinkedList(head)

def get_test_circular_ll_2():
	"""
	1 --> 2 --> 3 --> 4
	      ^           |
	      |           |
       	   -----------
	"""
	fourth_node = Node("D")
	third_node = Node("C", fourth_node)
	second_node = Node("B", third_node)
	head = Node("A", second_node)
	fourth_node.next = second_node #cycle

	return LinkedList(head)

def test_has_cycle_hashmap():
	normal_list1 = build_ll_from_lst([2,4,5])
	normal_list2 = build_ll_from_lst([1])
	circle_list1 = get_test_circular_ll_1()
	circle_list2 = get_test_circular_ll_2()
	assert has_cycle_hashmap(None) == False
	assert has_cycle_hashmap(normal_list1.head) == False
	assert has_cycle_hashmap(normal_list2.head) == False
	assert has_cycle_hashmap(circle_list1.head) == True
	assert has_cycle_hashmap(circle_list2.head) == True

def test_has_cycle_runners():
	normal_list1 = build_ll_from_lst([2,4,5])
	normal_list2 = build_ll_from_lst([1])
	circle_list1 = get_test_circular_ll_1()
	circle_list2 = get_test_circular_ll_2()
	assert has_cycle_runners(None) == False
	assert has_cycle_runners(normal_list1.head) == False
	assert has_cycle_runners(normal_list2.head) == False
	assert has_cycle_runners(circle_list1.head) == True
	assert has_cycle_runners(circle_list2.head) == True

def test_get_first_node_in_cycle():
	circle_list1 = get_test_circular_ll_1()
	circle_list2 = get_test_circular_ll_2()
	assert get_first_node_in_cycle(circle_list1.head) == 0
	assert get_first_node_in_cycle(circle_list2.head) == 1

def test_find_length_of_cycle():
	circle_list1 = get_test_circular_ll_1()
	circle_list2 = get_test_circular_ll_2()
	assert find_length_of_cycle(circle_list1.head) == 2
	assert find_length_of_cycle(circle_list2.head) == 2

if __name__ == "__main__":
	test_has_cycle_hashmap()
	test_has_cycle_runners()
	test_get_first_node_in_cycle()
	test_find_length_of_cycle()

