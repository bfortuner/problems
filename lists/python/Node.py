class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_next_node(self):
		return self.next_node

	def set_next_node(self, next_node):
		self.next_node = next_node


# Tests

def test_get_set_node():
	second_node = Node("B")
	first_node = Node("A", second_node)

	assert first_node.get_next_node() == second_node
	assert first_node.get_value() == "A"

	first_node.set_value("Z")
	new_node = Node("C", second_node)
	first_node.set_next_node(new_node)

	assert first_node.get_value() == "Z"
	assert first_node.get_next_node() == new_node

	next_node = first_node.get_next_node()
	assert next_node == new_node
	assert next_node.get_next_node() == second_node

	next_node = next_node.get_next_node()
	assert next_node == second_node
	assert next_node.get_next_node() is None

if __name__ == "__main__":
	print "Node tests starting!"
	test_get_set_node() 
	print "Node tests complete!"
