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
			linked_list_str = linked_list_str + cur_node.get_value() + "-"
			cur_node = cur_node.get_next_node()
		return linked_list_str


## Tests

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
	assert list_str == "A-B-C-"

#Run all Tests
print "LinkedList tests starting!"
test_build_linked_list()
test_get_linked_list_str()
print "LinkedList tests complete!"