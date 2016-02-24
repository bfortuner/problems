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

	def get_size(self):
		size = 0
		node = self.first_node
		while node is not None:
			size += 1
			node = node.get_next_node()
		return size

	def delete_kth_node(self, k):
		'''Delete 0th node means 1st node'''
		# A --> B --> C --> None
		i = 0
		node = self.get_first_node()
		if node is None:
			return
		if k == 0:
			self.set_first_node(node.get_next_node())
		while i < k-1 and node.get_next_node() is not None:
			node = node.get_next_node()
			i += 1
		if node.get_next_node() is not None:
			new_next_node = node.get_next_node().get_next_node()
			node.set_next_node(new_next_node)

	def contains_value(self, value):
		node = self.get_first_node()
		while node is not None:
			if node.get_value() == value:
				return True
			node = node.get_next_node()
		return False



#remove_node_after_cur_node(Node node)
#insert_value_after_node(Node node, String value)
#remove_node_by_value(Node first, String value)
#get_max_value_in_list_iterative(Node first)
#get_max_value_in_list_recursive(Node first)




## Helpers

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

def get_test_linked_list():
	third_node = Node("C")
	second_node = Node("B", third_node)
	first_node = Node("A", second_node)

	test_list = LinkedList(first_node)
	return test_list




# Tests

def test_build_ll_from_lst():
	lst1 = []
	lst2 = ["A"]
	lst3 = ["A","B"]

	ll1 = LinkedList()
	ll2 = LinkedList(Node("A"))
	ll3 = LinkedList(Node("A"))
	ll3.get_first_node().set_next_node(Node("B"))

	assert ll1.lists_eq(build_ll_from_lst(lst1))
	assert ll2.lists_eq(build_ll_from_lst(lst2))
	assert ll3.lists_eq(build_ll_from_lst(lst3))

def test_contains_value():
	l1 = build_ll_from_lst([])
	l2 = build_ll_from_lst(["A"])
	l3 = build_ll_from_lst(["A","B"])

	assert l1.contains_value("A") == False
	assert l2.contains_value("A") == True
	assert l2.contains_value("B") == False
	assert l3.contains_value("B") == True
	assert l3.contains_value("C") == False

def test_deleted_kth_node__empty_list():
	# None -->
	empty_list = LinkedList()
	empty_list.delete_kth_node(3)
	assert empty_list.get_first_node() is None

def test_deleted_kth_node__one_element():
	# A --> None
	first_node = Node("A")
	test_list = LinkedList(first_node)
	test_list.delete_kth_node(1)
	assert test_list.get_first_node() == first_node

	test_list.delete_kth_node(3)
	assert test_list.get_first_node() == first_node

	test_list.delete_kth_node(0)
	assert test_list.get_first_node() == None	

def test_deleted_kth_node__three_elements():
	# A --> B --> C --> None
	test_list = get_test_linked_list()
	test_list.delete_kth_node(4)
	test_list.delete_kth_node(3)
	test_list.delete_kth_node(1)
	test_list.delete_kth_node(0)
	assert test_list.get_first_node().get_value() == "C"

def test_get_size():
	test_list = get_test_linked_list()
	assert test_list.get_size() == 3

	empty_list = LinkedList()
	assert empty_list.get_size() == 0

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
test_get_size()
test_deleted_kth_node__empty_list()
test_deleted_kth_node__one_element()
test_deleted_kth_node__three_elements()
test_build_ll_from_lst()
test_contains_value()
print "LinkedList tests complete!"