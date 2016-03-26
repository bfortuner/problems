from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

"""
Sum Two Lists - Add two numbers together

Each number's digits are stored in a Single Linked List in reverse order 

(e.g. 134 == 4 --> 3 --> 1)
"""

def sum_two_lists(list1, list2):
	"""
	Numbers Digits Stored in Reverse Order
	(e.g. 134 == 4 --> 3 --> 1)
	"""
	node1 = list1.head
	node2 = list2.head
	digit = 1
	totalsum = 0
	while node1 is not None or node2 is not None:
		if node1 is not None:
			totalsum += (node1.value * digit)
			node1 = node1.next
		if node2 is not None:
			totalsum += (node2.value * digit)
			node2 = node2.next
		digit *= 10
	return totalsum


"""
Sum Two Lists - And return Linked List!

Each number's digits are stored in a Single Linked List in reverse order 

Approaches:
1) Keep track of cur_sum + carry. Create new Node + New List. Add cur sum to value. Move on.

Cases:
1) Both lists None
2) One list empty
3) One-node lists
4) Lists of different lengths
5) Lists of same length

Get last digit? (Modulo  by 10)
17 % 10 == 7

Get Carry Digit/ Remove last digit (Divide by 10)
17 / 10 = 1

"""

def sum_two_lists_return_list(list1, list2):
	sum_list = LinkedList(Node(None))
	local_sum = 0
	carry_digit = 0
	node1 = list1.head
	node2 = list2.head
	sum_node = sum_list.head
	while node1 is not None or node2 is not None:
		if node1 is not None:
			node1_val = node1.value
			node1 = node1.next
		else:
			node1_val = 0
		if node2 is not None:
			node2_val = node2.value
			node2 = node2.next
		else:
			node2_val = 0

		local_sum = node1_val + node2_val + carry_digit
		sum_node.value = local_sum % 10
		carry_digit = local_sum / 10
		sum_node.next = Node(None)  #Watch out! This appends None to end of every solution
		sum_node = sum_node.next
	return sum_list


def sum_two_lists_return_list_recursive(list1, list2):
	pass




"""
Sum Two Lists - Numbers Digits Stored in Proper Order

Approaches:
1) Strings - Loops through and append each value to a string.
Parse final string into an integer
2) Use two stacks. Loop through Linked Lists appending to each stack. 
Then keep track of digit and pop from each stack until empty multiplying
by current digit.
3) Use Python List (which could act like a stack)

"""

def sum_two_lists_proper_string(list1, list2):
	"""
	(e.g. 134 == 1 --> 3 --> 4)
	"""
	node1 = list1.head
	node2 = list2.head
	if node1 is None:
		sum1_str = "0"
	else:
		sum1_str = ""
	if node2 is None:
		sum2_str = "0"
	else:
		sum2_str = ""
	while node1 is not None:
		sum1_str += str(node1.value)
		node1 = node1.next
	while node2 is not None:
		sum2_str += str(node2.value)
		node2 = node2.next
	return int(sum1_str) + int(sum2_str)



# Tests

def test_sum_two_lists():
	list1 = build_ll_from_lst([])
	list2 = build_ll_from_lst([])
	assert sum_two_lists(list1,list2) == 0

	list1 = build_ll_from_lst([1])
	list2 = build_ll_from_lst([1])
	assert sum_two_lists(list1,list2) == 2

	list1 = build_ll_from_lst([5,3,1])
	list2 = build_ll_from_lst([5,2])
	assert sum_two_lists(list1,list2) == 160

def test_sum_two_lists_proper_string():
	list1 = build_ll_from_lst([])
	list2 = build_ll_from_lst([])
	assert sum_two_lists_proper_string(list1,list2) == 0

	list1 = build_ll_from_lst([1])
	list2 = build_ll_from_lst([1])
	assert sum_two_lists_proper_string(list1,list2) == 2

	list1 = build_ll_from_lst([5,3,1])
	list2 = build_ll_from_lst([5,2])
	assert sum_two_lists_proper_string(list1,list2) == 583

def test_sum_two_lists_return_list():
	list1 = build_ll_from_lst([])
	list2 = build_ll_from_lst([])
	outputlist = sum_two_lists_return_list(list1,list2)
	print outputlist.get_linked_list_str()
	answerlist = build_ll_from_lst([None])
	print answerlist.get_linked_list_str()
	assert answerlist.lists_eq(outputlist) == True 

	list1 = build_ll_from_lst([1])
	list2 = build_ll_from_lst([1])
	outputlist = sum_two_lists_return_list(list1,list2)
	print outputlist.get_linked_list_str()
	answerlist = build_ll_from_lst([2,None])
	assert answerlist.lists_eq(outputlist) == True 

	list1 = build_ll_from_lst([5,3,1])
	list2 = build_ll_from_lst([5,2])
	outputlist = sum_two_lists_return_list(list1,list2)
	print outputlist.get_linked_list_str()
	answerlist = build_ll_from_lst([0,6,1,None])
	print answerlist.get_linked_list_str()
	assert answerlist.lists_eq(outputlist) == True 

if __name__ == "__main__":
	test_sum_two_lists()
	test_sum_two_lists_proper_string()
	test_sum_two_lists_return_list()
