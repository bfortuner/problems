from Node import Node

class LinkedList:
	def __init__(self, first_node=None):
		self.first_node = first_node

	def set_first_node(self, new_first_node):
		self.first_node = new_first_node

	def get_first_node(self):
		return self.first_node

	def get_linked_list_str(self):
		linked_list_str = ""
		cur_node = self.first_node
		while cur_node is not None:
			linked_list_str = linked_list_str + cur_node.get_value() + "->"
			cur_node = cur_node.get_next_node()
		return linked_list_str

	def remove_last_node(self):
		node = self.first_node
		if node.get_next_node() == None:
			return
		while node.get_next_node().get_next_node() is not None:
			node = node.get_next_node()
		node.set_next_node(None)


	def lists_eq(self, other_list):
		'''
		Python by default checks if 
		two objects exist in same memory space
		'''
		if other_list == self:
			return True
		if not isinstance(other_list, LinkedList):
			return False
		node = self.get_first_node()
		other_node = other_list.get_first_node()
		while node is not None:
			if other_node is None:
				return False
			elif other_node.get_value() != node.get_value():
				return False
			node = node.get_next_node()
			other_node = other_node.get_next_node()
		return other_node is None





#get_size(Node first)
#delete_kth_node(Node first, int k)
#list_contains_value(Node first, String value)
#remove_node_after_cur_node(Node node)
#insert_value_after_node(Node node, String value)
#remove_node_by_value(Node first, String value)
#get_max_value_in_list_iterative(Node first)
#get_max_value_in_list_recursive(Node first)






def test_remove_last_node():
	#A -- > B -- > C --> None
	#A -- > B -- > None
	test_list = get_test_linked_list()
	second_node = Node("B")
	first_node = Node("A", second_node)
	answer_list = LinkedList(first_node)

	test_list.remove_last_node()
	assert(test_list.lists_eq(answer_list))

def test_lists_eq__same_object():
	node = Node("A")
	test_list = LinkedList(node)
	test_list_cp = test_list
	assert test_list.lists_eq(test_list_cp)
	assert test_list.lists_eq(test_list)

def test_lists_eq__other_not_instance_of_linked_list():
	node = Node("A")
	test_list = LinkedList(node)
	not_linked_list = "ABC"
	assert not test_list.lists_eq(not_linked_list)

def test_lists_eq__one_node():
	node = Node("A")
	test_list = LinkedList(node)
	other_list = LinkedList(node)
	assert test_list.lists_eq(other_list)

	other_node = Node("A")
	other_list2 = LinkedList(other_node)
	assert test_list.lists_eq(other_list2)

def test_lists_eq__lists_empty():
	test_list = LinkedList()
	other_list = LinkedList()
	assert test_list.lists_eq(other_list)

	node = Node("A")
	test_list.set_first_node(node)
	assert not test_list.lists_eq(other_list)
	assert not other_list.lists_eq(test_list)

def get_test_linked_list():
	third_node = Node("C")
	second_node = Node("B", third_node)
	first_node = Node("A", second_node)

	test_list = LinkedList(first_node)
	return test_list

def test_build_linked_list():
	test_list = get_test_linked_list()
	new_first_node = Node("Z")
	new_first_node.set_next_node(test_list.get_first_node())
	test_list.set_first_node(new_first_node)

	cur_node = test_list.get_first_node()
	assert cur_node.get_value() == "Z"

	cur_node = cur_node.get_next_node()
	assert cur_node.get_value() == "A"

	cur_node = cur_node.get_next_node()
	assert cur_node.get_value() == "B"

	cur_node = cur_node.get_next_node()
	assert cur_node.get_value() == "C"

	cur_node = cur_node.get_next_node()
	assert cur_node is None

def test_get_linked_list_str():
	test_list = get_test_linked_list()
	list_str = test_list.get_linked_list_str()
	assert list_str == "A->B->C->"

#Run all Tests
print "LinkedList tests starting!"
test_build_linked_list()
test_get_linked_list_str()
test_remove_last_node()
test_lists_eq__same_object()
test_lists_eq__other_not_instance_of_linked_list()
test_lists_eq__one_node()
test_lists_eq__lists_empty()
print "LinkedList tests complete!"